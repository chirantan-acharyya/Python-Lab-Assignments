n=int(input())

x=int(0)
y=int(0)
s=int(0)
i=int(0)
while n!=0:
    if i%2==0:
        x=x+int((n%10))
    else:
        y=y+int((n%10))
    i=i+1
    n=n/10

s=y-x
print(s)
