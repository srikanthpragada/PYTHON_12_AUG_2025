class Customer:
    def __init__(self, name, email):
        self.name = name
        # private attribute
        self.__email = email

    def show(self):
        print(self.name, self.__email)

c = Customer("Van Rossum", "van@microsoft.com")
#print(c._Customer__email)
#c._Customer__email = 'rossum@microsoft.com'
c.show()
print(c.__dict__)


