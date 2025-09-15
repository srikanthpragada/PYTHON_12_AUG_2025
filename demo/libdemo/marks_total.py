
f = open("marks.txt", "rt")

for line in f.readlines():
    parts = line.strip().split(",")
    if len(parts) < 2:
        continue   # ignore the line

    name = parts[0]
    #print(parts[1:])
    marks = filter(str.isdigit, parts[1:])
    total = sum(map(int, marks))
    print(f"{name:20} {total:3}")

f.close()


