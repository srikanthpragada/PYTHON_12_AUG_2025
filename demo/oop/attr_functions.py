class Circle:
    pass

c = Circle()
print(getattr(c, 'radius', 10))
setattr(c, 'x', 5)
print(hasattr(c, 'x'))
delattr(c, 'x')
print(hasattr(c, 'x'))
