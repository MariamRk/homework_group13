from number import Number

class IntegerNumber(Number):
    def __init__(self, value):
        self.value= int(value)

    def get_value(self):
        return self.value
    def add(self, number):
        self.value += number
        return self.nu
    def sub(self, number):
        self.value -= number
    def mul(self, number):
        self.value *= number
    def div(self, number):
        if number != 0:
            self.value /= number
        else :
            print('ნულზე გაყოფა არ შეიძლება')

