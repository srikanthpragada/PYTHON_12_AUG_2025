import re


with open("test.txt", "rt") as f:
    content = f.read()


with open("test.txt", "wt") as f:
    new_content = re.sub(r' +', ' ', content)
    f.write(new_content)



