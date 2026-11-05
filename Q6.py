menu = input("Enter menu: ").split()
price_str = input("Enter prices: ").split()
prices = []
for p in price_str:
    prices.append(int(p))

ordered = input("Enter ordered items: ").split()

total = 0
for i in range(len(menu)):
    item = menu[i]
    p = prices[i]
    
    count = 0
    for o in ordered:
        if o == item:
            count = count + 1
            
    if count > 0:
        cost = count * p
        total = total + cost
        print(item, "x", count, "=", cost)

print("Total:", total)