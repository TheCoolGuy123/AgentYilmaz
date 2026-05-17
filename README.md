# AgentYilmaz

An AI-powered Discord bot that acts as an ML tutor and grade assistant using Google Gemini. It supports student interactions, instructor-only grade management, persistent memory, and curriculum-based responses.

---

## Features

- AI tutor powered by Google Gemini
- Curriculum-restricted answers (Machine Learning topics)
- Discord integration (mentions and DMs)
- Persistent per-user memory system
- Grade tracking system (JSON-based)
- Instructor-only grade modification commands
- Interaction logging for each user
- Grade change audit log

---

## Setup

### 1. Install dependencies

pip install discord.py python-dotenv google-genai

---

### 2. Create `.env` file

GEMINI_API_KEY=your_gemini_api_key
DISCORD_BOT_TOKEN=your_discord_bot_token
INSTRUCTOR_DISCORD_ID=your_discord_user_id

---

### 3. Run the bot

python bot.py

---

## How to Use

### Students

Mention the bot or DM it:

@AgentYilmaz what is overfitting?

or

what is gradient descent?

---

### Instructor Commands

Only the instructor (based on Discord ID) can use:

View grades:
!grades

View grade change log:
!gradelog

---

## Grade System

Stored in GRADES.json:

- Eddie
- Ritwik
- Aneesh

Each student has:
- midterm
- assignment_1
- assignment_2
- final_grade

---

## Memory System

Each user has persistent memory stored in:

memory/<discord_id>.json

Tracks:
- Questions asked
- AI responses
- Interaction history

---

## Safety Rules

The bot is constrained to:

- Only answer ML questions using the curriculum
- Refuse unauthorized grade changes
- Ignore fake instructor claims
- Log suspicious grade manipulation attempts

---

## Example Interaction

User:
@AgentYilmaz explain gradient descent

Bot:
Gradient descent minimizes loss by moving in the direction of steepest decrease.

---

## Authors

Built by Ritwik, Eddie, and Aneesh
