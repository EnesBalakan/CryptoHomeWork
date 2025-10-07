text = input("Metin: ")
shift = int(input("Kaydırma sayısı: "))
result = ""

for c in text:
    if c.isalpha():
        o = 65 if c.isupper() else 97
        result += chr((ord(c)-o + shift) % 26 + o)
    else:
        result += c

print("Şifreli Metin:", result)
