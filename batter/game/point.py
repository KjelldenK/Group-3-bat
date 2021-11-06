
from game import constants

class Point:

    def __init__(self, x, y):

        self._x = x
        self._y = y


    def add(self, other):

        x = self._x + other.get_x()
        y = self._y + other.get_y()
        return Point(x,y)

    def equals(self, other):
        """Whether or not this Point is equal to the given one.

        Args:
            other (Point): The Point to compare.

        Returns: 
            boolean: True if both x and y are equal; false if otherwise.
        """
        return self._x == other.get_x() and self._y == other.get_y()

    def get_x(self):
        """Gets the horizontal distance.
        
        Returns:
            integer: The horizontal distance.
        """
        return self._x

    def get_y(self):
        """Gets the vertical distance.
        
        Returns:
            integer: The vertical distance.
        """
        return self._y

    def is_zero(self):
        """Whether or not the point is zero or x = 0 and y = 0.
        
        Returns:
            boolean: True if x = 0 and y = 0; false if otherwise.
        """
        return self._x == 0 and self._y == 0
    
    def is_boarder(self, leng):
        return self._x < 0 or self._x > constants.MAX_X - leng
        
    def reverse(self):
        """Gets a new Point that is the reverse of this one.
        
        Returns:
            Point: A new Point that is reversed.
        """
        x = self._x * -1
        y = self._y * -1
        return Point(x, y)


    def reverse_y(self):
        # reverse the y value 
        x = self._x
        y = self._y * -1
        return Point(x,y)
        
    def reverse_x(self):
        # reverse the x value
        x = self._x * -1
        y = self._y
        return Point(x,y)

