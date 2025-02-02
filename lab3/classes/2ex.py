"""
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("area equals", self.length * self.width
print("Enter length and width")
r = Rectangle(int(input()), int(input())
r.area()
"""

class shape:
    def __init__(self):
        pass
    def area(self):
        return 0
class square(shape):
    def __init__(self , length):
        super().__init__()
        self.length = length
    def area(self):
        return self.length**2
a = int(input())
answer = shape()
print('defoult area: ',answer.area())
inp_area = square(a)
print('Your area: ' , inp_area.area())