import json
import os

MEMORY_DIR = "memory"
os.makedirs(MEMORY_DIR, exist_ok=True)

def load_memory(student_id: str) -> dict:
    path = f"{MEMORY_DIR}/{student_id}.json"
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    return {
        "student_id": student_id,
        "history": [],
        "notes": ""
    }

def save_memory(student_id: str, memory: dict):
    path = f"{MEMORY_DIR}/{student_id}.json"
    with open(path, "w") as f:
        json.dump(memory, f, indent=2)

def add_interaction(student_id: str, question: str, reply: str):
    mem = load_memory(student_id)
    mem["history"].append({
        "question": question,
        "reply": reply
    })
    save_memory(student_id, mem)

def load_grades() -> dict:
    with open("GRADES.json", "r") as f:
        return json.load(f)

def save_grades(grades: dict):
    with open("GRADES.json", "w") as f:
        json.dump(grades, f, indent=2)

def change_grade(student_name: str, field: str,
                 new_value, changed_by: str) -> str:
    grades = load_grades()
    if student_name not in grades["students"]:
        return f"Student '{student_name}' not found."
    old_value = grades["students"][student_name].get(field, "N/A")
    grades["students"][student_name][field] = new_value
    grades["grade_change_log"].append({
        "student": student_name,
        "field": field,
        "old_value": old_value,
        "new_value": new_value,
        "changed_by": changed_by
    })
    save_grades(grades)
    return (f"Grade changed: {student_name} {field} "
            f"{old_value} → {new_value} (by {changed_by})")