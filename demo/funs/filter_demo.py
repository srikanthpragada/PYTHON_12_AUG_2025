
def iseven(n):
    return n % 2 == 0

nums = [10, 13, 25, 55,66,77,88]

for n in filter(iseven, nums):
    print(n)
