
#Write a python program to execute addition, subtraction, multiplication and
#division according to the choice of user. In case of division print an error
#message if divisor is zero, otherwise print quotient and remainder.

a=int(input("Enter First Number:\t"))
b=int(input("Enter Second Number:\t"))
c=int(input("Enter 1 for add\n 2 for subtract\n 3 for product\n 4 for division:  "))
out=int(0)
if c==1:
    out=a+b
    print("Sum= ",out)
elif c==2:
    out=a-b
    print("Difference= ",out)
elif c==3:
    out=a*b
    print("Product= ",out)
elif c==4:
    if b==0:
        print("Cannot be divided by Zero")
    else:
        print("Quotient= ",(a/b))
        print("Remainder= ",(a%b))
else:
    print("Invalid Input")