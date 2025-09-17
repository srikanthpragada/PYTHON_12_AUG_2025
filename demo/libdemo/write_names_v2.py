names = ["Scott",  "Richards", "Kathy", "Mark", "George"]

with open("names.txt", "wt" ) as f:
    for n in names:
        f.write(n + "\n")
