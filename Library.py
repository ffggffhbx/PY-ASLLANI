events = [
    ("borrow", "S01", "Python", 1),
    ("borrow", "S01", "Python", 2),
    ("return", "S01", "Python", 1),
    ("borrow", "S02", "Python", 1),
    ("return", "S03", "Python", 2),
    ("borrow", "S01", "Python", 1),
]


def process_events(events):
    # کلید: (title, copy_number)  =>  مقدار: student_id
    on_loan = {}

    # عنوان => مجموعهٔ دانشجویانی که با موفقیت آن عنوان را امانت گرفته‌اند
    borrowers_by_title = {}

    # رویدادهای ردشده: (شمارهٔ رویداد، خود رویداد، دلیل)
    rejected = []

    for index, event in enumerate(events, start=1):
        action, student_id, title, copy_number = event
        key = (title, copy_number)

        if action == "borrow":
            if key in on_loan:
                rejected.append(
                    (index, event, f"already on loan to {on_loan[key]}")
                )
            else:
                on_loan[key] = student_id
                borrowers_by_title.setdefault(title, set()).add(student_id)

        elif action == "return":
            if on_loan.get(key) == student_id:
                del on_loan[key]
            else:
                holder = on_loan.get(key)
                if holder is None:
                    reason = "copy is not on loan"
                else:
                    reason = f"copy is on loan to {holder}, not {student_id}"
                rejected.append((index, event, reason))

        else:
            rejected.append((index, event, "unknown action"))

    return on_loan, borrowers_by_title, rejected


on_loan, borrowers_by_title, rejected = process_events(events)

print("Current loans:")
for (title, copy_number), student_id in sorted(on_loan.items()):
    print(f"  {title} copy {copy_number}: {student_id}")

print("\nBorrowers per title:")
for title in sorted(borrowers_by_title):
    students = ", ".join(sorted(borrowers_by_title[title]))
    print(f"  {title}: {students}")

print("\nRejected events:")
for index, event, reason in rejected:
    print(f"  {index}: {event} -> {reason}")