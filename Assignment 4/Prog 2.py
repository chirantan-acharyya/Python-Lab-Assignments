# Rotate List by 1
l = list(map(int, input().split()))
x=l[len(l)-1]
for i in range(len(l)-1,0,-1):
    l[i]=l[i-1]

l[0]=x
print(l)