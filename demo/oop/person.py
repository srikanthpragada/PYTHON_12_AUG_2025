class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}  - {self.age}"

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __gt__(self, other):
        return self.age > other.age

    def __int__(self):
        return self.age


p1 = Person("Van Rossum", 55)
p2 = Person("Van Rossum", 55)
p3 = Person("James Gosling", 60)

print(p1 == p2)  # p1.__eq__(p2)
print(p3 > p2)   # p1.__gt__(p2)
print(p1 < p3)   # p1.__gt__(p2)

print(int(p1) + int(p3))



# print(p1)
# print(str(p1))
# print(p1.__str__())
