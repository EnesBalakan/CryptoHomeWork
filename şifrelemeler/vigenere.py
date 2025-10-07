text = input("Metin: ")
key = input("Anahtar kelime: ")
result = ""
j = 0

for c in text:
    if c.isalpha():
        o = 65 if c.isupper() else 97
        k = ord(key[j % len(key)].lower()) - 97
        result += chr((ord(c)-o + k) % 26 + o)
        j += 1
    else:
        result += c

print("Şifreli Metin:", result)
