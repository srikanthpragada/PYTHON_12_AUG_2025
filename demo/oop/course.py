
class Course:
    #Static or class attributes
    taxrate = 10

    @staticmethod
    def set_taxrate(newrate):
        Course.taxrate = newrate

    def __init__(self, title, duration = 24, fee = 0 ):
        # Object Attributes
        self.title = title
        self.duration = duration
        self.fee = fee

    def show(self):
        print('Title:', self.title)
        print('Duration:', self.duration)
        print('Fee:', self.fee)

    def get_net_fee(self):
        return self.fee + (self.fee *  Course.taxrate // 100)

    def set_fee(self, newfee):
        if newfee >= 0:
            self.fee = newfee
        else:
            raise ValueError('Invalid Fee. It must be >= 0')

Course.set_taxrate (12)

# Create an object (instance)
c1 = Course("Generative AI", fee = 10000)
c1.show()
c1.set_fee(12500)
print('Net Fee:', c1.get_net_fee())

