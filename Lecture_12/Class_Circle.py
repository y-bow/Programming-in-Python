
class Circle:
    def __init__(self, x = 0, y = 0, r = 0):
        self.__x = x
        self.__y = y
        self.__r = r
    def circle_details(self):
        print(f"Circle of radius {self.__r} at ({self.__x}, {self.__y})")

    def circle_properties(self):
        peri = 2 * 3.14 * self.__r
        area = 3.14 * self.__r * self.__r
        print(f"{peri} is the Perimeter of the circle")
        print(f"{area:.2f} is the Area of the circle")

    def circle_move(self, new_x, new_y):
        self.__x = new_x
        self.__y = new_y
    
    def radius_change(self, new_r):
        self.__r = new_r

c = Circle(1.0, 2.0, 3.0)
c.circle_details()
c.circle_properties()
c.circle_move(5.0, 6.0)
c.circle_details()
c.radius_change(5.0)
c.circle_details()