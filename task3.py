from math import sqrt


class Shape:
    def __init__(self, radius=1):
        self.coordinates = (0, 0)
        self.radius = radius

    def get_distance(self, figure_1, figure_2):
        x1, y1 = figure_1.coordinates
        x2, y2 = figure_2.coordinates
        return sqrt((x1 - x2)**2 + (y1 - y2)**2)


class Circle(Shape):
    def get_center(self):
        """
        Get (x, y) coordinates of circle
        :return: tuple<int>
        """
        return self.coordinates

    def move(self, x, y):
        """
        Mutate coordinates of circle
        :param x: int
        :param y: int
        """
        self.coordinates = (x, y)

    def get_area(self):
        """
        Calculates area of circle
        :return: float
        """
        radius = self.radius
        return 3.14 * (radius * radius)


class Triangle(Shape):
    def get_center(self):
        """
        Get (x, y) coordinates of triangle
        :return: tuple<int>
        """
        return self.coordinates

    def move(self, x, y):
        """
        Mutate coordinates of triangle
        :param x: int
        :param y: int
        """
        self.coordinates = (x, y)

    def get_area(self):
        """
        Calculates area of triangle
        :return: float
        """
        return 3 * sqrt(3) * self.radius

    def get_vertex(self):
        """
        Return a number of vertexes of triangle
        :return int
        """
        return 3


class Square(Shape):
    def get_center(self):
        """
        Get (x, y) coordinates of triangle
        :return: tuple<int>
        """
        return self.coordinates

    def move(self, x, y):
        """
        Mutate coordinates of triangle
        :param x: int
        :param y: int
        """
        self.coordinates = (x, y)

    def get_area(self):
        """
        Calculates area of triangle
        :return: float
        """
        radius = self.radius
        return 4 * (radius * radius)

    def get_vertex(self):
        """
        Return a number of vertexes of triangle
        :return int
        """
        return 4


circle_instance = Circle(5)
print('Circle radius {}'.format(circle_instance.radius))
circle_instance.move(2, 2)
print('Circle coordinates {}'.format(circle_instance.coordinates))
print('Circle area {}'.format(circle_instance.get_area()))
print('Circle center {}'.format(circle_instance.get_center()))

triangle_instance = Triangle(3)
print('Triangle radius {}'.format(triangle_instance.radius))
triangle_instance.move(-1, 1)
print('Triangle coordinates {}'.format(triangle_instance.coordinates))
print('Triangle area {}'.format(triangle_instance.get_area()))
print('Triangle center {}'.format(triangle_instance.get_center()))
print('Triangle vertexes {}'.format(triangle_instance.get_vertex()))

square_instance = Square(2)
print('Square radius {}'.format(square_instance.radius))
square_instance.move(8, -5)
print('Square coordinates {}'.format(square_instance.coordinates))
print('Square area {}'.format(square_instance.get_area()))
print('Square center {}'.format(square_instance.get_center()))
print('Square vertexes {}'.format(square_instance.get_vertex()))

print('Distance of Square and Circle: {}'.format(square_instance.get_distance(square_instance, circle_instance)))
