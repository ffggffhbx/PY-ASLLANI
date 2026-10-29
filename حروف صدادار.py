word = input("یک کلمه انگلیسی وارد کنید: ")
count = 0

for ch in word:
    if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
        count = count + 1
    elif ch == "A" or ch == "E" or ch == "I" or ch == "O" or ch == "U":
        count = count + 1

print("تعداد حروف صدادار:", count)