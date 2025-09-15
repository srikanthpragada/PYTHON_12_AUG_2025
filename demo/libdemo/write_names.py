names = ["Scott",  "Richards", "Kathy", "Mark", "George"]

# 1. Create
f = open("names.txt", "wt" )

# 2. Write
for n in names:
    f.write(n + "\n")

# 3. Close
f.close()
