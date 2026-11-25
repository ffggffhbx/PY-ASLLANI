films = ["F1", "F2", "F3", "F4"]

votes = [
    ("S01", "F2"),
    ("S02", "F1"),
    ("S01", "F2"),
    ("S01", "F1"),
    ("S03", "F1"),
    ("S04", "F2"),
    ("S02", "F3"),
    ("S05", "F2"),
]


def process_votes(films, votes):
    # تعداد رأی‌های معتبر هر فیلم
    valid_count = {film: 0 for film in films}

    # دانشجویانی که به هر فیلم رأی معتبر داده‌اند
    voters = {film: set() for film in films}

    # اولین موقعیت رأی معتبر برای هر فیلم، برای شکستن تساوی
    first_valid_position = {film: None for film in films}

    # جفت‌های (دانشجو، فیلم) که قبلاً دیده شده‌اند
    seen_pairs = set()

    # ارسال‌های تکراری: (موقعیت، دانشجو، فیلم)
    duplicates = []

    for position, (student, film) in enumerate(votes, start=1):
        pair = (student, film)

        if pair in seen_pairs:
            duplicates.append((position, student, film))
            continue

        seen_pairs.add(pair)

        valid_count[film] += 1
        voters[film].add(student)

        if first_valid_position[film] is None:
            first_valid_position[film] = position

    film_order = {film: i for i, film in enumerate(films)}

    def sort_key(film):
        # فیلم‌های بدون رأی در انتها و به ترتیب فهرست films
        if valid_count[film] == 0:
            return (1, film_order[film], 0)

        # ابتدا تعداد رأی بیشتر، سپس اولین رأی معتبر زودتر
        return (0, -valid_count[film], first_valid_position[film])

    ranked_films = sorted(films, key=sort_key)

    return valid_count, voters, duplicates, ranked_films


valid_count, voters, duplicates, ranked_films = process_votes(films, votes)

print("جدول نتایج:")
print("رتبه | فیلم | تعداد رأی معتبر")
print("-" * 35)

for rank, film in enumerate(ranked_films, start=1):
    print(f"{rank:^5} | {film:^4} | {valid_count[film]:^16}")

print("\nارسال‌های تکراری:")
for position, student, film in duplicates:
    print(f"موقعیت {position}: دانشجو {student} دوباره به فیلم {film} رأی داده است.")

top1 = ranked_films[0]
top2 = ranked_films[1]

both_voted = voters[top1] & voters[top2]

print(f"\nدو فیلم رتبهٔ اول و دوم: {top1} و {top2}")
print("دانشجویانی که به هر دو رأی معتبر داده‌اند:")
print(sorted(both_voted))