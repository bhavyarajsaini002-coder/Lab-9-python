s = input("Enter numbers: ")
lst = s.split()

even = []
odd = []

for x in lst:
    num = int(x)
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Even:", even)
print("Odd:", odd)