#Write a python program to find the maximum and minimum number in a list of
#10 elements and also find the index position of the following numbers.

l1 = list(map(int, input().split()))
max=int(l1[0])
maxpos=int(0)
min=int(l1[0])
minpos=int(0)

for i in l1:
    if(max<i):
        max=i
        maxpos=l1.index(i)
    if(min>i):
        min=i
        minpos=l1.index(i)

print("Min Element is ",min," present at ",minpos," position")
print("\nMax Element is ",max," present at ",maxpos," position")



