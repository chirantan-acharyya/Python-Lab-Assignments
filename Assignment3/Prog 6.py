#6. Find the second maximum from a list of integers.
#Input/output:
#User will give a list of integers
#the program will print the second maximum of the list.
#In case of multiple occurrence of maximum value or a single number in the list, the
#second maximum will be also the maximum number.

l = list(map(int, input().split()))
l.sort()
print(l[-2])

