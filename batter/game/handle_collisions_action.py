from game.action import Action
from game.point import Point
from game import constants
from game.score import Score
class HandleCollisionsAction(Action):
    


    def execute(self, cast):
        # executes the action to see if any object are hit eachother and changing there status due to collisions.
       
        ball = cast["ball"][0]
        paddle = cast["paddle"][0] 
        bricks = cast["brick"]
        score = cast["score"][0]

        # makes sure the paddle cant go off the screen
        if paddle.get_position().is_boarder(len(paddle.get_text())):
            position = paddle.get_position()
            velocity = paddle.get_velocity()
            x1 = position.get_x()
            y1 = position.get_y()
            x2 = velocity.get_x() * -1
            y2 = velocity.get_y()
            x = 1 + (x1 + x2 - 1)
            y = 1 + (y1 + y2 - 1)
            position = Point(x,y)
            paddle.set_position(position)

        # check in the ball is hitting a wall of a brick and if its a brick its removed and a score is added
        for brick in bricks:
            if ball.get_position().equals(brick.get_position()):
                points = brick.get_points()
                score.add_score(points)
                bricks.remove(brick)
                ball.set_velocity(Point.reverse_y(ball.get_velocity()))

        if ball.get_position().get_y() == paddle.get_position().get_y():
            if ball.get_position().get_x() >= paddle.get_position().get_x() and ball.get_position().get_x() <= (paddle.get_position().get_x() + 11):
                ball.set_velocity(Point.reverse_y(ball.get_velocity()))

        if ball.get_position().get_y() == 0:
            ball.set_velocity(Point.reverse_y(ball.get_velocity()))
        
        if ball.get_position().get_x() == 0 or ball.get_position().get_x() == constants.MAX_X:
            ball.set_velocity(Point.reverse_x(ball.get_velocity()))

        if ball.get_position().get_y() == constants.MAX_Y:
            quit()


