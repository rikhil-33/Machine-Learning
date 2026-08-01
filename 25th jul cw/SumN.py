#sum of n nums
n = int(input("Enter num of values: "))
total = 0
for i in range(n):
    num = int(input("Enter a num: "))
    total += num
print(total)