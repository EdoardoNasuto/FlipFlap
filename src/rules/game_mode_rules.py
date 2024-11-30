from src.rules.params_rule import *
from src.rules.game_rules import *


def base_game(num_rows, num_columns, num_obstacles, num_balls, size):
    GameRules(num_rows, num_columns, num_obstacles, num_balls, size,
              obstacle_setup=ItemSetup.RANDOM, ball_setup=ItemSetup.RANDOM, item_type=ItemnType.BALLS,
              obstacle_color={"red": 0.34,
                              "blue": 0.33, "green": 0.33},
              ball_out_of_the_board=BallOutOfTheBoard.DELETE)


def trap_game(num_rows, num_columns, num_obstacles, num_balls, size):
    GameRules(num_rows, num_columns, num_obstacles, num_balls, size,
              obstacle_setup=ItemSetup.EQUALLY, ball_setup=ItemSetup.RANDOM, item_type=ItemnType.BALLS,
              obstacle_color={"red": 0.40, "blue": 0.30,
                              "green": 0.20, "white": 0.10},
              obstacle_in_game_color_change={"red": 0.40, "blue": 0.30,
                                             "green": 0.30},
              ball_out_of_the_board=BallOutOfTheBoard.TRAVERSE_BOARD,
              change_obstacle_color_if_ball_present=ChangeObstacleColor.RANDOM,
              change_obstacle_color_on_click=ChangeObstacleColor.RANDOM)


def poule_renard_vipere_game(num_rows, num_columns, num_obstacles, num_balls, size):
    GameRules(num_rows, num_columns, num_obstacles, num_balls, size,
              obstacle_setup=ItemSetup.RANDOM, ball_setup=ItemSetup.EQUALLY, item_type=ItemnType.ANIMALS,
              obstacle_color={"red": 0.30, "blue": 0.30,
                              "green": 0.30, "purple": 0.10},
              obstacle_in_game_color_change={
                  "red": 0.34, "blue": 0.33, "green": 0.33},
              ball_out_of_the_board=BallOutOfTheBoard.TRAVERSE_BOARD,
              change_obstacle_color_if_ball_present=ChangeObstacleColor.RANDOM,
              ball_collision=BallCollision.SIMULATE_FOOD_CHAIN)
