
def pretty(n):
    return int(n) if n == int(n) else n


def show_history(history):
    if len(history) == 0:
        print("تاریخچه خالی است")
        return
    print("تاریخچه:")
    for i in range(len(history)):
        print("  " + str(i + 1) + ") " + history[i])


def to_base(value, fn):
 
    if value != int(value):
        print("فقط اعداد صحیح قابل تبدیل هستند")
    else:
        print(fn(int(value)))


def calc(a, op, b):
    if op == "+": return a + b
    if op == "-": return a - b
    if op == "*": return a * b
    if op == "/":
        if b == 0:
            print("تقسیم بر صفر مجاز نیست")
            return None
        return a / b
    if op == "**": return a ** b
    print("عملگر نامعتبر")
    return None



history = []
memory = 0
last = 0

print("دستورات: h=تاریخچه  b/o/x=مبنا  m+/m/m-=حافظه  c=ریست کامل  q=خروج")
print("محاسبه: 5 + 3   یا   2 ** 10")
print("-" * 50)

while True:
    s = input("> ")

    if s == "q":
        break

    if s == "c":
        history = []
        memory = 0
        last = 0
        print("\033[2J\033[H", end="")
        print("دستورات: h=تاریخچه  b/o/x=مبنا  m+/m/m-=حافظه  c=ریست کامل  q=خروج")
        print("محاسبه: 5 + 3   یا   2 ** 10")
        print("-" * 50)
        continue

    if s == "h":
        show_history(history)
        continue

    if s == "m":
        print("حافظه:", pretty(memory))
        continue

    if s == "m+":
        memory = memory + last
        print("حافظه:", pretty(memory))
        continue

    if s == "m-":
        memory = memory - last
        print("حافظه:", pretty(memory))
        continue

    if s == "b":
        to_base(last, bin)
        continue
    if s == "o":
        to_base(last, oct)
        continue
    if s == "x":
        to_base(last, hex)
        continue

    
    parts = s.split()

    
    if len(parts) == 1:
        try:
            last = float(parts[0])
            print("=", pretty(last))
            history.append(s + " = " + str(pretty(last)))
        except ValueError:
            print("عدد نامعتبر")
        continue

    
    if len(parts) != 3:
        print("فرمت اشتباه! مثال: 5 + 3")
        continue

    try:
        a = float(parts[0])
        b = float(parts[2])
    except ValueError:
        print("عدد نامعتبر")
        continue

    result = calc(a, parts[1], b)
    if result is None:
        continue

    last = result
    print("=", pretty(last))
    history.append(s + " = " + str(pretty(last)))