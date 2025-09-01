def morethan1upper(name):
    count = 0
    for c in name:
        if c.isupper():
            count += 1

    return count > 1


name = ['ELLison', 'Mark', 'George', 'Marshall', 'SAM']

for n in filter(morethan1upper, name):
    print(n)
