from game.point import Point
from game import constants
class Actor:

    def __init__(self):
        self._text = ""
        self._position = Point(0,0)
        self._velocity = Point(0,0)
        self._points = int

    def set_position(self, position):
        """sets the acotrs position in 2d space
        """
        self._position = position

    def set_text(self, text):
        """sets the acotrs text.
        """

        self._text = text

    def set_velocity(self, velocity):
        """sets the acotrs velocity
        """
        self._velocity = velocity

    def get_position(self):
        # get the position of the actor

        return self._position

    def get_velocity(self):
        # get the velocity of the actor
        return self._velocity

    def get_text(self):
        # get the text of the actor
        return self._text


        """     def get_hitbox(self):
        hit_box = {}

        position = self.get_position()

        # get the hit box above the ball object
        x = position.get_x() 
        y = position.get_y() -1
        hit_box["upper"] = [Point(x,y)]

        # get the hit box under the ball
        x = position.get_x() 
        y = position.get_y() + 1
        hit_box["bottom"] = [Point(x,y)]

        # get the hit box to the right of the ball object
        x = position.get_x() + 1
        y = position.get_y() 
        hit_box["upper"] = [Point(x,y)]

        # get the hit box to the left of the ball
        x = position.get_x() - 1
        y = position.get_y() 
        hit_box["bottom"] = [Point(x,y)]

        return hit_box """

    def set_points(self, points):
        # sets the points for an object
        self._points = points
    
    def get_points(self):
        # get the points that an object is worth
        return self._points


