class Figure:
    def __init__(self, color=(255, 255, 255)):
        self.__sides = []
        self.__color = list(color)
        self.filled = False

    def get_color(self):
        return self.__color

    def set_color(self, r, g, b):
        if all(isinstance(c, int) and 0 <= c <= 255 for c in (r, g, b)):
            self.__color = [r, g, b]

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if all(isinstance(side, int) and side > 0 for side in new_sides) and len(new_sides) == self.sides_count:
            self.__sides = list(new_sides)

    def __len__(self):
        return sum(self.__sides)

class Circle(Figure):
    sides_count = 1

    def __init__(self, color=(255, 255, 255), radius=1):
        super().__init__(color)
        self.set_sides(radius)

    def get_square(self):
        radius = self.get_sides()[0]
        return 3.14 * (radius ** 2)

class Triangle(Figure):
    sides_count = 3

    def __init__(self, color=(255, 255, 255), a=1, b=1, c=1):
        super().__init__(color)
        self.set_sides(a, b, c)

    def get_square(self):
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5

class Cube(Figure):
    sides_count = 12

    def __init__(self, color=(255, 255, 255), edge_length=1):
        super().__init__(color)
        self.set_sides(*([edge_length] * self.sides_count))

    def get_volume(self):
        edge_length = self.get_sides()[0]
        return edge_length ** 3

# Проверка кода
circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())

cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())

circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга):
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())