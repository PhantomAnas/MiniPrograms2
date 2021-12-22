
# x = 1 + 2i
# y = 2 + 3i

class Complex:
    def __init__(self, num):
        self.r = num.rsplit(' ', 2)[0]
        self.i_ = num.rsplit(' ', 1)[1]
        self.i = self.i_.rsplit('i')[0]
    def __add__(self, other):
        real = int(self.r) + int(other.r)
        img_ = int(self.i) + int(other.i)
        img = str(img_) + 'i'
        complex = str(real) + ' + ' + img
        return complex
    def __sub__(self, other):
        real = int(self.r) - int(other.r)
        img_ = int(self.i) - int(other.i)
        img = str(img_) + 'i'
        complex = str(real) + ' + ' + img
        return complex
    def __mul__(self, other):
        real = int(self.r) * int(other.r)
        img_ = int(self.i) * int(other.i)
        img = str(img_) + 'i'
        complex = str(real) + ' + ' + img
        return complex
    def __div__(self, other):
        real = int(self.r) / int(other.r)
        img_ = int(self.i) / int(other.i)
        img = str(img_) + 'i'
        complex = str(real) + ' + ' + img
        return complex
    def __repr__(self):
        return f"By Repr: {self.r + ' + ' + self.i + 'i'}"
    def __str__(self):
        return f"By Str: {self.r + ' + ' + self.i + 'i'}"

while True:
    in1 = input('Enter Number 1: ')
    in2 = input('Enter Number 2: ')
    c1 = Complex(in1)
    c2 = Complex(in2)
    print("Press 1 to Add\nPress 2 to Subtract\nPress 3 to Multiply \nPress 4 to Divide")
    opcode = int(input("Enter: "))
    if opcode == 1:
        print(c1+c2)
    elif opcode == 2:
        print(c1-c2)
    elif opcode == 3:
        print(c1*c2)
    elif opcode == 4:
        print(c1/c2)
    else:
        print("Invalid")
    print(repr(c1))
    print(str(c2))

