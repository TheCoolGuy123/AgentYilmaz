import discord
import os
import json
from dotenv import load_dotenv

load_dotenv()

from agent import ask_agentyilmaz
from memory import load_grades


INSTRUCTOR_ID = os.getenv("INSTRUCTOR_DISCORD_ID")
DISCORD_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

if not DISCORD_TOKEN:
    raise ValueError("Missing DISCORD_BOT_TOKEN in .env")


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"AgentYilmaz is online as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    student_id = str(message.author.id)

    username = message.author.display_name

    content = message.content.strip()

    is_instructor = (str(message.author.id) == INSTRUCTOR_ID)


    if content == "!gradelog" and is_instructor:
        grades = load_grades()
        log = grades.get("grade_change_log", [])

        if not log:
            await message.channel.send("No grade changes logged.")
        else:
            text = "\n".join([
                f"{e['changed_by']} changed {e['student']} "
                f"{e['field']}: {e['old_value']} → {e['new_value']}"
                for e in log
            ])
            await message.channel.send(f"```\n{text}\n```")
        return

    if content == "!grades" and is_instructor:
        grades = load_grades()
        await message.channel.send(
            f"```json\n{json.dumps(grades['students'], indent=2)}\n```"
        )
        return

    if (client.user.mentioned_in(message) or
            isinstance(message.channel, discord.DMChannel)):

        async with message.channel.typing():
            reply, grade_changed = ask_agentyilmaz(
                student_id, username, content, is_instructor
            )

            if grade_changed:
                await message.channel.send(
                    f"{reply}\n\n**[Grade change recorded in log]**"
                )
            else:
                await message.channel.send(reply)


client.run(DISCORD_TOKEN)