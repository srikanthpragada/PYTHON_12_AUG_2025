def show(**kwargs):
    for k, v in kwargs.items():
        print(k, '->', v)


def showall(*args, **kwargs):
    pass


show(name='Python', ver="3.13")
show(firstname='Srikanth', email='srikanth@srikanthtechnologies.com')
showall(1, 2, 3, name="Python")
