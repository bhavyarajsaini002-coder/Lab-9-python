s = input("Enter numbers: ").split()
nums = []
for x in s:
    nums.append(int(x))

largest = nums[0]
smallest = nums[0]

for n in nums:
    if n > largest:
        largest = n
    if n < smallest:
        smallest = n

print("Largest:", largest)
print("Smallest:", smallest)