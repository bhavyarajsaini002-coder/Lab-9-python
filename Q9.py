n = int(input("Enter N: "))
names_list = []

for i in range(n):
    line = input()
    parts = line.split()
    first = parts[0].lower()
    last = parts[1].lower()
    
    base = first + "." + last
    
    count = 0
    for name in names_list:
        if name == base:
            count = count + 1
            
    names_list.append(base)
    
    if count == 0:
        print(base + "@jklu.edu.in")
    else:
        print(base + str(count + 1) + "@jklu.edu.in")