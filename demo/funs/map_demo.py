def firstchar(name):
    return name[0].upper()

names = ['Ellison', 'mark', 'george', 'Marshall']

for v in map(len, names):
    print(v)

for v in map(firstchar, names):
    print(v)

for v in map(lambda n : n[0].upper(), names):
    print(v)

