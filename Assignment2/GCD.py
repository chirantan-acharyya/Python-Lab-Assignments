# Write a python program to find GCD of two numbers.

def gcd(a, b):    #GCD is the user Defined Function
  if(b == 0):
        return a
  else:
        return gcd(b, a % b)  

a=int(input("Enter two numbers:\t"))
b=int(input())

print('GCD =',gcd(a,b))