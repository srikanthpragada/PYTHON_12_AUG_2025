import os

allfiles = os.walk(r"c:\classroom\python\demo")
total_count = 0
for (dirname, folders, files) in allfiles:
    print("Directory :", dirname)
    print("=" * 50)
    count = 0
    for file in files:
        if file.endswith(".py"):
            print(file)
            count += 1
    print(f'Count = {count}')
    print('-' * 50)
    total_count += count

print('*' * 80)
print(f'Total count = {total_count}')
