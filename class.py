class Triangle():
    def __init__(self, bottom, height):
        self.bottom = bottom
        self.height = height

    def area(self):
        return self.bottom * self.height // 2

triangle_instance1 = Triangle(10, 10)
print(triangle_instance1.area())