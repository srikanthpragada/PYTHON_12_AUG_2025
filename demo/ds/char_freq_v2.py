st = "how do yo do"
d = {}

for c in st:
    if c not in d:
        d[c] = st.count(c)

print(d)



