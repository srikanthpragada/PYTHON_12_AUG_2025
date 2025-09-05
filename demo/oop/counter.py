class Counter:
    # constructor
    def __init__(self, value = 0):
        # Object Attributes
        self.value = value

    def inc(self, step = 1):
        self.value += step

    def dec(self):
        self.value -= 1

    def get_value(self):
        return self.value


# Create an object of Counter
c = Counter()
# Call Methods
c.inc(5)
c.inc()
#print(c.value)
print(c.get_value())

c2 = Counter(100)
# Call Methods
c2.dec()
print(c2.get_value())