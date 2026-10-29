word = input("یک کلمه انگلیسی وارد کنید: ")
result = ""

for ch in word:
    if ch >= "a" and ch <= "z":
        result = result + chr(ord(ch) - 32)
    else:
        result = result + ch

print(result)