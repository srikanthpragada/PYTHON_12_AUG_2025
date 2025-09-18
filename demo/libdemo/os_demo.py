import os

print(os.getcwd())

for file in os.listdir():
    print(file)

print(os.getenv('PATH'))