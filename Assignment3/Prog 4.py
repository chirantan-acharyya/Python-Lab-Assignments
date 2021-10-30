#Find the sum of the following series without using any function from math
#module:
#1-x+x 2 - x 3 +…(-1) n x n, n = 0, 1, 2…
#Input/output:
#User will give input for n and x, the output will be the sum of the above series.
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