class WindowDlg:
    def __init__(self, title, width, height):
        self.__title = title
        self.__width = width
        self.__height = height

    def show(self):
        print(f'"{self.__title}: {self.__width}, {self.__height}"')

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) == int and 1000 >= width >= 0:
            self.__width = width
            self.show()

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) == int and 1000 >= height >= 0:
            self.__height = height
            self.show()
    
a = WindowDlg('123',123,231)