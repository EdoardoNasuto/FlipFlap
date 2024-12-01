from src.rules.params_rule import *
from src.controllers.game_controller import GameController
from src.controllers.setup_controller import SetupController
from src.models.obstacle_model import Obstacle
from src.models.ball_model import Ball
from time import sleep

from typing import Optional


class GameRules ():
    def __init__(self, num_rows: int, num_columns: int, num_obstacles: int, num_balls: int, size: int, speed: float,

                 obstacle_setup: ItemSetup, ball_setup: ItemSetup, item_type: ItemnType,

                 obstacle_color: dict,
                 obstacle_in_game_color_change: Optional[dict] = None,

                 ball_out_of_the_board: Optional[BallOutOfTheBoard] = None,
                 change_obstacle_color_on_click: Optional[ChangeObstacleColor] = None,
                 change_obstacle_color_if_ball_present: Optional[ChangeObstacleColor] = None,
                 ball_collision: Optional[BallCollision] = None,

                 players: int = None,
                 players_choices: list[Optional[PlayerChoices]] = None,
                 ):

        def setup_game():
            Obstacle.available_colors = obstacle_color
            setup_controller.setup_model(
                obstacle_setup, ball_setup, item_type)
            setup_controller.setup_view()

        def run_game():

            game.view.refresh()

            if obstacle_in_game_color_change != None:
                game.model.obstacle_colors = obstacle_in_game_color_change

            while game.model.balls:
                sleep(speed)
                if players:
                    game.players_turn(players, players_choices)

                for ball in list(game.model.balls):

                    if change_obstacle_color_if_ball_present:
                        game.change_obstacle_color_if_ball_present(
                            ball, change_obstacle_color_on_click)

                    if not game.move_ball(ball):
                        if ball_out_of_the_board == BallOutOfTheBoard.DELETE:
                            game.remove_ball(ball)
                        if ball_out_of_the_board == BallOutOfTheBoard.TRAVERSE_BOARD:
                            game.ball_traverse_board(ball)

                    if change_obstacle_color_on_click:
                        game.change_obstacle_color_on_click(
                            change_obstacle_color_on_click)

                if ball_collision == BallCollision.SIMULATE_FOOD_CHAIN:
                    game.simulate_food_chain()

                game.view.refresh()
            game.view.exit_game()

        setup_controller = SetupController(
            num_rows, num_columns, num_obstacles, num_balls, size)
        setup_game()

        game = GameController(
            setup_controller.model, setup_controller.view)
        run_game()
