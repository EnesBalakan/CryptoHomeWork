text = input("Metin: ")
a = int(input("a (a ve 26 aralarında asal olmalı): "))
b = int(input("b: "))
result = ""

for c in text:
    if c.isalpha():
        o = 65 if c.isupper() else 97
        result += chr((a*(ord(c)-o)+b) % 26 + o)
    else:
        result += c

print("Şifreli Metin:", result)
