# Write a menu driven python program to implement a calculator that can 
# perform four basic
# mathematical operations – addition, subtraction, multiplication 
# and division (showing quotient and remainder).

a=int(input("Enter two numbers:\t"))
b=int(input())

c=int(input("Enter 1 for addition\n2 for subtraction\n3 for multiplication\n4 for division\t"))

if c==1:
    print('\nSum=',(a+b))
elif c==2:
    print('\nDifference=',(a-b))    
elif c==3:
    print('\nProduct=',(a*b))    
elif c==4:
    print('\nQuotient=',(a/b))  
    print('\nRemainder=',(a%b))
else:
    print('\nInvalid Operator')
