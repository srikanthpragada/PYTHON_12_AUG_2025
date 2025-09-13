r = range(5)
ri = r.__iter__()

for n in r:
    print(n)

while True:
    try:
        print(ri.__next__())
    except:
        break

while True:
    try:
        print(ri.__next__())
    except:
        break
