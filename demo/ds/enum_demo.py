lst = [10,20,30]

idx = 0
for n in lst:
    print(idx, n)
    idx += 1

# enumerate returns tuple, which is unpacked
for i, v in enumerate(lst):
    print( i, v)

