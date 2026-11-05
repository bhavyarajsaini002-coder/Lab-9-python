sent = input("Enter sentence: ")
words = sent.split()
ans = []

for w in words:
    if len(w) > 3:
        ans.append(w)

print(ans)