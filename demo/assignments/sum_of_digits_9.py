def sumdigit(num):
      digitsum = sum(map(int, str(num)))
      return digitsum == 9

num = [9,18,20, 207, 117]

for i in filter(sumdigit, num):
    print(i)