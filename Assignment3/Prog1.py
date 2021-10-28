
x=int(input("Enter Value of x:\t"))
n=int(input("Enter Value of n:\t"))
s=float(1)
for i in range(1,n+1):
    prod=pow(x,i)
    if i%2==1:
       s=s-prod
    else:
       s=s+prod
print("sum= ",s,sep=" ")