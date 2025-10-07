text = input("Metin: ")
key = "qwertyuiopasdfghjklzxcvbnm"
result = ""

for c in text:
    if c.isalpha():
        o = 65 if c.isupper() else 97
        result += key[ord(c.lower())-97].upper() if c.isupper() else key[ord(c)-97]
    else:
        result += c

print("Şifreli Metin:", result)
