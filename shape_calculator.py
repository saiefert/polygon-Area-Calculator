class Rectangle:
    def __init__(self, width, height):
        self.name = "Rectangle"
        self.width = width
        self.height = height

    def __str__(self):
        return f'{self.name}(width={self.width}, height={self.height})'

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return 'Too big for picture.'

        picture = ''
        cont = self.height

        while cont > 0:
            picture += '*' * self.width + '\n'
            cont -= 1

        return picture

    def get_amount_inside(self, shape):
        area_shape = shape.height * shape.width       
        return int(self.get_area() / area_shape)


class Square(Rectangle):
    def __init__(self, side):
        self.name = "Square"
        self.width = side
        self.height = side
        
    def __str__(self):
        return f'{self.name}(side={self.width})'

    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.width = height
        self.height = height

    def set_side(self, side):
        self.width = side
        self.height = side

