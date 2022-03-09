import cycle.constants

from cycle.casting.cast import Cast
from cycle.casting.food import Food
from cycle.casting.score import Score
from cycle.casting.snake import Snake
from cycle.scripting.script import Script
from cycle.scripting.control_actors_action import ControlActorsAction
from cycle.scripting.move_actors_action import MoveActorsAction
from cycle.scripting.handle_collisions_action import HandleCollisionsAction
from cycle.scripting.draw_actors_action import DrawActorsAction
from cycle.directing.director import Director
from cycle.services.keyboard_service import KeyboardService
from cycle.services.video_service import VideoService
from cycle.shared.color import Color
from cycle.shared.point import Point


def main():
    
    # create the cast
    cast = Cast()
    cast.add_actor("foods", Food())
    cast.add_actor("snakes", Snake())
    cast.add_actor("scores", Score())
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()