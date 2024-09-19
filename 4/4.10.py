class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c


class EquilateralTriangle(Triangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length, side_length)


# Пример использования
triangle = Triangle(3, 4, 5)
print("Perimeter of triangle:", triangle.perimeter())
equilateral_triangle = EquilateralTriangle(4)
print("Perimeter of equilateral triangle:", equilateral_triangle.perimeter())