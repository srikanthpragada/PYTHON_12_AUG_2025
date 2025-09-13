class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if self.isempty():
            raise ValueError('Stack is empty!')

        return self.data.pop()

    def peek(self):
        return self.data[-1]

    def isempty(self):
        return self.length() == 0

    @property
    def length(self):
        return len(self.data)

    def clear(self):
        self.data.clear()


s = Stack()
s.push(10)
s.push(20)
print(s.peek())
print(s.length)
