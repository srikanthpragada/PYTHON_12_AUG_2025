st = "how do yo do"

d = {}

for c in sorted(set(st)):
    d[c] = st.count(c)

print(d)



