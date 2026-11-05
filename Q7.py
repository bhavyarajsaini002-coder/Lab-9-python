sent = input("Enter sentence: ")
words = sent.split()
final_list = []

for w in words:
    rev = ""
    for ch in w:
        rev = ch + rev
    final_list.append(rev)

print(" ".join(final_list))