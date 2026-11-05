s = input("Enter numbers: ").split()
nums = []
for x in s:
    nums.append(int(x))

ans = []
zeros = 0

for n in nums:
    if n != 0:
        ans.append(n)
    else:
        zeros = zeros + 1

for i in range(zeros):
    ans.append(0)

print(ans)