nums = [10, 13, 25, 55, 66, 77, 88]

for n in filter(lambda n: n % 2 == 0, nums):
    print(n)
