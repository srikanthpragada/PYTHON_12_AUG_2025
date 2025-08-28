def isprime(num):
    for i in range(2, num//2 + 1):
        if num % i == 0:
            return False  # terminate and return false

    return True

print(isprime(13), isprime(50))