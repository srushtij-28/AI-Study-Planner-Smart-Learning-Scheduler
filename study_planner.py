from datetime import datetime

subjects = []

def add_subject():
    name = input("Subject name: ")
    exam = input("Exam date (YYYY-MM-DD): ")
    difficulty = int(input("Difficulty (1–5): "))

    exam_date = datetime.strptime(exam, "%Y-%m-%d")
    days_left = (exam_date - datetime.now()).days

    weight = difficulty / max(1, days_left)

    subjects.append({
        "name": name,
        "days": days_left,
        "difficulty": difficulty,
        "weight": weight
    })

def show_plan():
    sorted_subjects = sorted(subjects, key=lambda x: x["weight"], reverse=True)
    print("\n📚 AI Study Plan")
    for s in sorted_subjects:
        print(f"{s['name']} | Days Left: {s['days']} | Priority Score: {s['weight']:.2f}")

while True:
    print("\n — AI Study Planner")
    print("1. Add Subject")
    print("2. Show Study Plan")
    print("3. Exit")

    c = input("Choose: ")
    if c == "1":
        add_subject()
    elif c == "2":
        show_plan()
    elif c == "3":
        break
