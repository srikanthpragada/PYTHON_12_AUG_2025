class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f"Radius = {self.radius}"

    def __gt__(self, other):
        return self.radius > other.radius


# Create list of circle objects
circles = [Circle(10), Circle(5), Circle(20)]

for c in sorted(circles):
    print(c)


