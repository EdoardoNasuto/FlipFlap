from time import sleep

from src.controllers.game_controller import GameController
from src.controllers.setup_controller import SetupController
from src.models.obstacle_model import Obstacle
from src.models.ball_model import Ball


def base_game_setup(game: SetupController):
    game.setup_model(random_obstacle=True, random_balls=True)
    game.setup_view()


def base_game(game: GameController) -> None:
    """
    Logique spécifique au mode de jeu 'base'.
    """
    while game.model.balls:
        sleep(game.speed)
        for ball in list(game.model.balls):
            if not game.move_ball(ball):
                game.remove_ball(ball)
        game.view.refresh()


def trap_game_setup(game: SetupController):
    Obstacle.available_colors = {"red": 0.40,
                                 "blue": 0.30, "green": 0.20, "white": 0.10}
    game.setup_model(random_obstacle=False, random_balls=False)
    game.setup_view()


def trap_game(game: GameController) -> None:
    """
    Logique spécifique au mode de jeu 'trap'.
    """
    game.model.obstacle_colors = {"red": 0.50, "blue": 0.30, "green": 0.20}
    while game.model.balls:
        sleep(game.speed)
        for ball in list(game.model.balls):
            game.change_obstacle_color_if_ball_present(ball, "random")
            if not game.move_ball(ball):
                game.ball_traverse_board(ball)
            game.change_obstacle_color_on_click("random")
        game.view.refresh()


def poule_renard_vipere_game_setup(game: SetupController):
    Obstacle.available_colors = {"red": 0.30,
                                 "blue": 0.30, "green": 0.30, "purple": 0.10}
    game.setup_model(random_obstacle=True, random_balls=True, animal=True)
    game.setup_view()


def poule_renard_vipere_game(game: GameController) -> None:
    """
    Logique spécifique au mode de jeu 'base'.
    """
    game.model.obstacle_colors = {"red": 0.34, "blue": 0.33, "green": 0.33}
    while game.model.balls:
        sleep(game.speed)
        for ball in list(game.model.balls):
            if not game.move_ball(ball):
                game.ball_traverse_board(ball)
        game.simulate_food_chain()
        game.view.refresh()
