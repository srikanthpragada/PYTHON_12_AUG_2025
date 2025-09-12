
total = 0
while True:
    try:
        num = int(input("Enter number [0 to stop] :"))
        if num == 0:
            break   # terminate loop
        total += num
    except ValueError as e:
        print('Sorry!Invalid Number. Try again!')

print("Total =", total)

