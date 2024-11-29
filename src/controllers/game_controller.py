from random import choice, choices

from src.views.game_view import GameView
from src.models.grid_model import Grid
from src.models.ball_model import Ball
from src.models.obstacle_model import Obstacle
from src.rules.params_rule import *


class GameController:
    """
    Gère la logique de contrôle pour la simulation, incluant la grille, les obstacles, les billes et l'interface graphique.

    Attributes:
        model (Grid): La grille contenant les obstacles et les billes.
        view (GameView): L'interface graphique pour afficher la simulation.
        speed (float): La vitesse de la simulation, par défaut 0.1.
    """

    def __init__(self, grid: Grid, gui: GameView):
        """
        Initialise le contrôleur avec une grille, une vue, et configure les obstacles et billes.

        Args:
            grid (Grid): L'instance de la grille utilisée pour la simulation.
            gui (GameView): L'interface graphique pour la simulation.
        """
        self.model = grid
        self.view = gui

    def move_ball(self, ball: Ball) -> bool:
        """
        Met à jour la position d'une bille et interagit avec les obstacles.
        """
        x1, y1 = ball.x, ball.y
        dx, dy = ball.move(test=True)
        if self.model.is_valid_position(x1 + dx, y1 + dy):
            ball.move()
            self.view.update_ball_position(
                ball.object_view, x1, y1, ball.x, ball.y)
            self.update_ball_direction(ball)
            return True
        return False

    def update_ball_direction(self, ball: Ball) -> None:
        """
        Gère l'interaction entre une bille et un obstacle.
        """
        obstacle = self.model.grid[ball.y][ball.x]
        if obstacle:
            effect = obstacle.affect_ball(ball)
            if effect == "delete":
                self.remove_ball(ball)
                ball = False
            elif effect == "new_ball":
                new_ball = self.model.add_ball(
                    ball.x, ball.y,
                    (self.model.ball_directions[((self.model.ball_directions.index(
                        ball.direction) + 2) % 4)]),
                    ball.animal)
                new_ball.object_view = self.view.draw_ball(
                    new_ball, f"assets/{ball.animal}.png")
                self.view.update_ball_direction(new_ball)
                ball = False
        if ball:
            self.view.update_ball_direction(ball)

    def change_obstacle_color_on_click(self, mode: str) -> None:
        """
        Gère les entrées de l'utilisateur, comme les clics sur la grille.
        """
        clic = self.view.recup_clic()
        if clic:
            obstacle = self.model.grid[clic.y //
                                       self.view.size][clic.x // self.view.size]
            if obstacle:
                self._change_obstacle_color(obstacle, mode)

    def change_obstacle_color_if_ball_present(self, ball: Ball, mode=str) -> None:
        """
        Gère l'interaction entre une bille et un obstacle.
        """
        obstacle = self.model.grid[ball.y][ball.x]
        if obstacle:
            # Si la bille est en contact avec un obstacle, change la couleur
            self._change_obstacle_color(obstacle, mode)

    def _change_obstacle_color(self, obstacle: Obstacle, mode) -> None:
        """
        Change la couleur d'un obstacle.
        """

        colors = list(self.model.obstacle_colors.keys())

        if obstacle.color in colors:
            if mode == ChangeObstacleColor.RANDOM:
                colors.remove(obstacle.color)
                obstacle.color = choice(colors)

            elif mode == ChangeObstacleColor.WEIGHTED:
                weights = list(self.model.obstacle_colors.values())
                weights.pop(colors.index(obstacle.color))
                colors.remove(obstacle.color)
                obstacle.color = choices(colors, weights=weights, k=1)[0]

            elif mode == ChangeObstacleColor.SEQUENTIAL:
                new_color = (colors.index(obstacle.color)+1) % len(colors)
                obstacle.color = colors[new_color]

            self.view.update_obstacle_color(
                obstacle.object_view, obstacle.color)

    def remove_ball(self, ball: Ball):
        """
        Supprimer une bille du model et de la view
        """
        self.view.remove_ball(ball.object_view, ball.direction_view)
        self.model.remove_ball(ball)

    def ball_traverse_board(self, ball: Ball):
        """
        Fait traverser la grille à la bille
        """
        x1, y1 = ball.x, ball.y
        ball.traverse_board(self.model.num_columns-1, self.model.num_rows-1)
        self.view.update_ball_position(
            ball.object_view, x1, y1, ball.x, ball.y)
        self.update_ball_direction(ball)

    def simulate_food_chain(self):
        dir = {
            "left": (-1, 0),
            "right": (1, 0),
            "up": (0, -1),
            "down": (0, 1)
        }

        for ball in list(self.model.balls):
            for other_ball in list(self.model.balls):
                if other_ball is not ball:

                    if ball.x == other_ball.x:
                        if ball.y == other_ball.y:
                            if ((self.model.ball_animals.index(ball.animal) - 1) % len(self.model.ball_animals)) == self.model.ball_animals.index(other_ball.animal):
                                self.remove_ball(ball)

                    # Regarde unquement la case voisine qui est dans sa direction
                    elif (ball.x + dir[ball.direction][0] + self.model.num_columns) % self.model.num_columns == other_ball.x:
                        if (ball.y + dir[ball.direction][1] + self.model.num_rows) % self.model.num_rows == other_ball.y:
                            # Vérifie que l'animal voisin et la direction oposé de la sienne (va le traverser)
                            if self.model.ball_directions[(self.model.ball_directions.index(ball.direction) + 2) % 4] == other_ball.direction:
                                # Verifie si l'animal doit etre mangé ou pas
                                if ((self.model.ball_animals.index(ball.animal) - 1) % len(self.model.ball_animals)) == self.model.ball_animals.index(other_ball.animal):
                                    self.remove_ball(ball)
