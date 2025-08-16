# Print numbers between 1 to 100 that are divisible either by 3 or 7

for n in range(3, 101):
    if n % 3 == 0 or n % 7 == 0:
        print(n, end = ' ')

