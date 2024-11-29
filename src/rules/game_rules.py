from src.rules.params_rule import *
from src.controllers.game_controller import GameController
from src.controllers.setup_controller import SetupController
from src.models.obstacle_model import Obstacle
from src.models.ball_model import Ball
from time import sleep

from typing import Optional


class GameRules ():
    def __init__(self, num_rows: int, num_columns: int, num_obstacles: int, num_balls: int, size: int,
                 obstacle_setup: ItemSetup, ball_setup: ItemSetup, item_type: ItemnType, obstacle_color: dict,
                 obstacle_in_game_color_change: Optional[dict] = None,
                 ball_out_of_the_board: Optional[BallOutOfTheBoard] = None,
                 change_obstacle_color_on_click: Optional[ChangeObstacleColor] = None,
                 change_obstacle_color_if_ball_present: Optional[ChangeObstacleColor] = None,
                 ball_collision: Optional[BallCollision] = None
                 ):

        self.obstacle_setup = obstacle_setup
        self.ball_setup = ball_setup
        self.item_type = item_type
        self.obstacle_color = obstacle_color
        self.obstacle_in_game_color_change = obstacle_in_game_color_change

        self.ball_out_of_the_board = ball_out_of_the_board
        self.change_obstacle_color_on_click = change_obstacle_color_on_click
        self.change_obstacle_color_if_ball_present = change_obstacle_color_if_ball_present
        self.ball_collision = ball_collision

        self.setup_controller = SetupController(
            num_rows, num_columns, num_obstacles, num_balls, size)
        self.setup_game()

    def setup_game(self):
        Obstacle.available_colors = self.obstacle_color
        self.setup_controller.setup_model(
            self.obstacle_setup, self.ball_setup, self.item_type)
        self.setup_controller.setup_view()

    def run_game(self):
        self.game = GameController(
            self.setup_controller.model, self.setup_controller.view, 0)

        self.game.view.refresh()

        if self.obstacle_in_game_color_change != None:
            self.game.model.obstacle_colors = self.obstacle_in_game_color_change

        while self.game.model.balls:
            sleep(1)

            for ball in list(self.game.model.balls):

                if self.change_obstacle_color_if_ball_present:
                    self.game.change_obstacle_color_if_ball_present(
                        ball, self.change_obstacle_color_on_click)

                if not self.game.move_ball(ball):
                    if self.ball_out_of_the_board == BallOutOfTheBoard.DELETE:
                        self.game.remove_ball(ball)
                    if self.ball_out_of_the_board == BallOutOfTheBoard.TRAVERSE_BOARD:
                        self.game.ball_traverse_board(ball)

                if self.change_obstacle_color_on_click:
                    self.game.change_obstacle_color_on_click(
                        self.change_obstacle_color_on_click)

            if self.ball_collision == BallCollision.SIMULATE_FOOD_CHAIN:
                self.game.simulate_food_chain()

            self.game.view.refresh()
        self.game.view.exit_game()
