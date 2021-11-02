n=input()
sum=0
for i in range(1,len(n),2):
    sum=sum+(int(n[i])*int(n[i]))

if(int(sum%9)==0):
    print("Lucky")
else:
    print("Unlucky")