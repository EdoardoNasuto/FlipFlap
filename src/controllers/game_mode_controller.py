from time import sleep

from src.controllers.game_controller import GameController
from src.models.obstacle_model import Obstacle


def base_game_setup():
    pass


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


def trap_game_setup():
    Obstacle.available_colors = {"red": 0.40,
                                 "blue": 0.30, "green": 0.20, "white": 0.10}


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
