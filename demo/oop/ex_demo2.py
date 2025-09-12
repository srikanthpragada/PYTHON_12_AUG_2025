
l = [1, 3, 0]
try:
    i = 2
    print(10 // l[i])
except IndexError:
    print('Sorry! Index outside the range!')
except ZeroDivisionError:
    print("Sorry! Division by 0 is not allowed!")

print("The End")


