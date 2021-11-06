from game.point import Point
from game.actor import Actor
class Score(Actor):

    def __init__(self):
        self._score = 0
        self._position = Point(1,20)
        self.set_text(f"score: {self._score}")
        self._velocity = Point(0,0)

    def add_score(self, points):
        # adds the points from the object to self._score
        self._score += points
        self.set_text(f"Score: {self._score}")

    def get_score(self):
        # gets the score fro the game
        return self._score
