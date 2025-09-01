def reverse_str(names):
    return names[::-1]


names = ['Ellison', 'Mark', 'George', 'Marshall']

for v in map(reverse_str, names):
    print(v)
