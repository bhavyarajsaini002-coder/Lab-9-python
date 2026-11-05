text = input("Enter string: ")
digits = []
s = 0

for ch in text:
    if ch >= '0' and ch <= '9':
        d = int(ch)
        digits.append(d)
        s = s + d

print(digits)
print("Sum:", s)