import json

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def show(self):
        print(self.name, self.email)

    def getdict(self):
        return { "fullname" : self.name.upper(), "email" : self.email}

c = Customer("Larry Page", "larry@google.com")
print(json.dumps(c.getdict()))
