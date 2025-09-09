class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(self.name)
        print(self.salary)

    def get_salary(self):
        return self.salary


class Manager(Employee):
    def __init__(self, name, salary, hra):
        super().__init__(name, salary)
        self.hra = hra

    def show(self):  # Overrides show()
        super().show()
        print(self.hra)

    def get_salary(self):  # Overrides get_salary()
        return super().get_salary() + self.hra

    def set_hra(self, hra):
        self.hra = hra

e = Employee("Scott", 100000)
m = Manager("Mike", 150000, 50000)
e.show()
print("Net Salary : ", e.get_salary())

m.set_hra(60000)
m.show()
print("Net Salary : ", m.get_salary())