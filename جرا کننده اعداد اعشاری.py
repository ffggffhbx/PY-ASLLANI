num = float(input("یک عدد اعشاری وارد کنید: "))

integer_part = int(num)
decimal_part = int((num - integer_part) * 10)

result = (decimal_part * 100) + (integer_part * 10)

print("نتیجه:", result)