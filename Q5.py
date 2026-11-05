sent = input("Enter sentence: ")
words = sent.split()

long_word = words[0]

for w in words:
    if len(w) > len(long_word):
        long_word = w

print(long_word)