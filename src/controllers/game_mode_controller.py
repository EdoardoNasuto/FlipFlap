from time import sleep

from src.controllers.game_controller import GameController


def base_game(game: GameController) -> None:
    """Logique spécifique au mode 'base'."""
    while game.model.balls:
        sleep(game.speed)
        for ball in list(game.model.balls):
            if not game.update_ball_position(ball):
                game.remove_ball(ball)


def trap_game(game: GameController) -> None:
    """Logique spécifique au mode 'trap'."""
    while game.model.balls:
        sleep(game.speed)
        for ball in list(game.model.balls):
            game.interact_with_obstacle(ball)
            if not game.update_ball_position(ball):
                game.remove_ball(ball)
            game.handle_user_input()
