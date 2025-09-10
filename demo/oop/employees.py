from abc import abstractmethod, ABC

# Abstract class
class Employee(ABC):
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def show(self):
        print(self.name)
        print(self.email)

    @abstractmethod
    def get_salary(self):
        pass


class SalariedEmployee(Employee):
    def __init__(self, name, email, salary):
        super().__init__(name, email)
        self.salary = salary

    def show(self):
        super().show()
        print(self.salary)

    def get_salary(self):
        return self.salary

class Consultant(Employee):
    def __init__(self, name, email, hour_rate, hours_worked):
        super().__init__(name, email)
        self.hour_rate = hour_rate
        self.hours_worked = hours_worked

    def show(self):
        super().show()
        print(self.hour_rate)
        print(self.hours_worked)

    def get_salary(self):
        return self.hours_worked * self.hour_rate

se = SalariedEmployee('James', 'james@gmail.com', 1500000)
print("Salary : ", se.get_salary())

c = Consultant("Larry", "larry@google.com", 10, 2000)
c.show()
print(c.get_salary())
