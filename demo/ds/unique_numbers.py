# Take 5 numbers and display unique ones
l = []    # Empty list

for i in range(5):
    num = int(input("Enter number :"))
    if num not in l:  # new number?
       l.append(num)

for n in l:
    print(n, end=' ')
