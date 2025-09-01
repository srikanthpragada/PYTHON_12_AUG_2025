def isbigname(name):
    print('Callled with ', name)
    return len(name) > 5

names = ['Ellison', 'Mark', 'George', 'Marshall']

for n in filter(isbigname, names):
    print(n)

for c in filter(str.isupper , 'How Are You?'):
     print(c)

