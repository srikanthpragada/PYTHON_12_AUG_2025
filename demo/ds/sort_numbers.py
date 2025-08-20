l = []

for i in range(5):
    num = int(input("Enter number :"))
    l.append(num)

l.sort()

for n in l:
    print(n, end=' ')
