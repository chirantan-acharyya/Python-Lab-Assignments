
def sum_postive_numbers(sum):

    if sum==1:
        return 1
    return sum+sum_postive_numbers(sum-1)

n = int(input())
print(sum_postive_numbers(n))