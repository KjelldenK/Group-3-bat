from time import sleep
from game import constants

class Director:
    
    def __init__(self, cast, script):

        self._cast = cast
        self._script = script


    def start_game(self):
        # game loop
        while True:
            self._cue_action("input")
            self._cue_action("update")
            self._cue_action("output")
            sleep(constants.FRAME_LENGTH)

    def _cue_action(self, tag):
        # perfroms the actions of the game.
        for action in self._script[tag]:
            action.execute(self._cast)