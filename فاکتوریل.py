num = int(input("یک عدد صحیح وارد کنید: "))
factorial = 1

for i in range(1, num + 1):
    factorial = factorial * i

print("فاکتوریل:", factorial)