# Display the following pattern
#           *
#         * * *
#       * * * * *
#         * * * 
#           *

n=int(3)
for i in range(1,n+1): 
    for sp in range(1,n-i+1):
        print(' ',end='')
    for j in range(1,(i*2)):
        print('*',end='')        
    print('\n')    

for i in range(n,1,-1):       
    for sp in range(0,n-i+1):
        print(' ',end='')
    for j in range(1,((i-1)*2)):
        print('*',end='')        
    print('\n')  

