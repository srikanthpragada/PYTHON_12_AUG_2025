# Generator
def numbers():
    for n in range(1, 6):
        yield n


g = numbers()
print(type(g))

print(next(g))
print(next(g))

# for v in g:
#     print(v)

gen = (n for n in range(1, 4))

print(type(gen))