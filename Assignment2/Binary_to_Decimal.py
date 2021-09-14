# Write a python program to convert a binary number to its decimal equivalent.

n=int(input("Enter a Number:\t"))

sum=int(0)
k=int(1)

while n!=0:
        sum+=int(n%10)*k
        k=k*2
        n=n/10

print('Decimal Equivalent=\t',sum)        