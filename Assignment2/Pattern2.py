# Display the following pattern
#           *
#         * *
#       * * *
#     * * * *
#   * * * * *

n=int(5)
for i in range(1,n+1): 
    for sp in range(1,n-i+1):
        print(' ',end='')
    for j in range(1,i+1):
        print('*',end='')
    print('\n')    
