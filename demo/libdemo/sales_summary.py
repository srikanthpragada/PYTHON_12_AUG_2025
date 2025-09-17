f = open('sales.txt', "rt")

for line in f.readlines():
    parts = line.strip().split(",")
    if len(parts) < 2:
        continue

    pname = parts[0]
    sales = list(filter(lambda v : v.strip().isdigit(), parts[1:]))
    total = sum(map(int, sales))
    print(f"{pname:30}  {total // len(sales):5}")

f.close()
