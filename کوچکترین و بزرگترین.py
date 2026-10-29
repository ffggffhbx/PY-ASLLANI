big = None
small = None

for i in range(10):
    num = int(input("عدد " + str(i + 1) + ": "))
    if big is None or num > big:
        big = num
    if small is None or num < small:
        small = num

print("بزرگ‌ترین:", big)
print("کوچک‌ترین:", small)