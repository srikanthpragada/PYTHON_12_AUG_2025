import sys

if len(sys.argv) < 2:
    print('Sorry! Number is missing. Run the program by providing number!')
    exit(1)  # Exit with error

num = int(sys.argv[1])

isprime = True

for i in range(2, num//2 + 1):
    if num % i == 0: # found a factor
        isprime = False
        break

if isprime:
    print('Prime number')
else:
    print('Not a prime number')






