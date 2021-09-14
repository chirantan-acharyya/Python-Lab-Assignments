# Display the following pattern
#   * * * * *    
#     * * * *    
#       * * *
#         * *
#           *

n=int(5)
for i in range(n+1,1,-1): 
    for sp in range(0,n-i+1):
        print(' ',end='')
    for j in range(1,i):
        print('*',end='')
    print('\n')    
