# Write a python program to check whether a number is even or odd without using modulus (%)
#operator.

n=int(input("Enter a Number:\t"))

if n&1==1:
    print('Number is Odd')
else:
    print('Number is Even')     