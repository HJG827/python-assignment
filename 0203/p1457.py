# 아래 클래스를 수정하시오.
class Shape:
    def __init__(self, width,height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height
    
    def calculate_perimeter(self):
        return (self.height + self.width) * 2
    
    def print_info(self):
        print(f'Width: {self.width}')
        print(f'Height: {self.height}')
        print(f'Area: {Shape.calculate_area(self)}')
        print(f'Perimeter: {Shape.calculate_perimeter(self)}')



shape1 = Shape(5, 3)
shape1.print_info()
