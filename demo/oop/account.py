class  InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount

    def __str__(self):
        return f"Withdraw for {self.amount} cannot be honoured with {self.balance} account balance"

class Account:
    #class attribute
    minbalance = 5000

    @staticmethod
    def set_minbalance(balance):
        Account.minbalance = balance

    def __init__(self, acno, ahname, balance):
        self.acno = acno
        self.ahname = ahname
        if balance < Account.minbalance:
            raise ValueError('Minimum Balance is not provided!')

        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('Deposit amount must be >= 1')

        self.balance += amount

    def withdraw(self, amount):
        if self.balance - Account.minbalance >= amount:
            self.balance -= amount
        else:
            raise InsufficientFundsError(self.balance, amount)

    def get_balance(self):
        return self.balance

a1 = Account(1, 'Larry Gomes', 5000)
a2 = Account(2, 'George Koch', 10000)
a1.deposit(10000)
a1.withdraw(20000)
print(a1.get_balance())
