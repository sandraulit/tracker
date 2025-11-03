from datetime import datetime
from pathlib import Path

DATA_FILE = Path("data/moods.txt")

def add_mood(mood):
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(DATA_FILE, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M')} - {mood}\\n")
    print(f"Mood '{mood}' recorded successfully!")

def view_moods():
    if not DATA_FILE.exists():
        print("No moods recorded yet.")
        return
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        print(\"\\nYour mood history:\\n\" + f.read())
