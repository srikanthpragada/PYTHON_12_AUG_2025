
st = "python is fun"

chars = []
for c in st:
    if c not in chars:
        chars.append(c)

for c in sorted(chars):
    print(c, end = '')


