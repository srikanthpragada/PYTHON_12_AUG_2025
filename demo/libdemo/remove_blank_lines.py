
with open("names.txt", "rt") as f:
   non_blank_lines = filter(lambda line: len(line.strip()) > 0, f.readlines())

with open("names.txt", "wt") as f:
    for line in non_blank_lines:
        f.write(line)




