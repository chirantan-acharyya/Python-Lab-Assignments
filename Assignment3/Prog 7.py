#7. Find the alternative subtraction and addition of numbers from a list of integers.
#Input/Output:
#User will give a space separated list of integers.
#Output:
#The program will keep adding all odd position numbers and then subtracting all even position numbers.

s1 = 0
s2 = 0
l1 = list(map(int, input().split()))
for i in range(len(l1)):
    if i & 1 == 1:
        s1 = s1 + l1[i]     # odd index
    else:
        s2 = s2 + l1[i]     # even index
print(s2 - s1)
