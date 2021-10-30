#5. Find the difference of sum of even digits and odd digits of a positive number.
#Input/output:
#User will give the number as input. If there are k numbers of even digits and m
#numbers of odd digits then the output will be(sum of k even digits)-(sum of m odd
#                                                                     digits).
n = int(input())

x = int(0)
y = int(0)
s = int(0)
i=int(0)
while n != 0:
    i = n % 10
    if i % 2 == 0:
        x = x + i
    else:
        y = y + i
    n = n/10

s = y-x
print(s)


