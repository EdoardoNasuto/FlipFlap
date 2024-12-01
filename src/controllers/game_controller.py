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

    # ------------------- Public Methods -------------------

    def move_ball(self, ball: Ball) -> bool:
        """
        Met à jour la position d'une bille et interagit avec les obstacles.

        Args:
            ball (Ball): La bille à déplacer.

        Returns:
            bool: True si la bille a été déplacée avec succès, sinon False.
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
        Gère l'interaction entre une bille et un obstacle, et met à jour sa direction.

        Args:
            ball (Ball): La bille dont la direction doit être mise à jour.
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
                self.view.update_ball_direction_arrow(new_ball)
                ball = False
        if ball:
            self.view.update_ball_direction_arrow(ball)

    def players_turn(self, n: int, player_choises: list) -> None:
        """
        Gère les actions des joueurs pendant leur tour.

        Args:
            n (int): Le nombre de joueurs à prendre en compte.
            player_choices (list): Les choix de chaque joueur sous forme de liste.
        """
        for player in range(n):
            index = self.view.listbox_popup(player,
                                            [choices[0].value for choices in player_choises])

            if player_choises[index][0] == PlayerChoices.CHANGE_OBSTACLE_COLOR:
                self.change_obstacle_color_on_click(
                    player_choises[index][1], True)
            if player_choises[index][0] == PlayerChoices.ADD_OBSTACLE:
                self.add_obstacle(player_choises[index][1], "black")

    def add_obstacle(self, mode, color) -> None:
        """
        Ajoute un obstacle sur la grille après avoir reçu un clic de l'utilisateur.

        Args:
            mode (str): Le mode de changement de couleur de l'obstacle.
            color (str): La couleur de l'obstacle à ajouter.
        """
        clic = self.view.attend_clic()
        if self.model.grid[clic.x//self.view.size][clic.y//self.view.size] == None:
            obstacle: Obstacle = self.model.add_obstacle(clic.x//self.view.size,
                                                         clic.y//self.view.size, color)
            obstacle.object_view = self.view.draw_obstacle(
                obstacle.x, obstacle.y, color)
            self.view.window.placerAuDessous(obstacle.object_view)
            self._change_obstacle_color(obstacle, mode, True)
            self.view.refresh()
        else:
            self.add_obstacle(mode, color)

    def change_obstacle_color_on_click(self, mode: str, blocking: bool = False) -> None:
        """
        Gère le changement de couleur d'un obstacle lors d'un clic de l'utilisateur.

        Args:
            mode (str): Le mode de changement de couleur.
            blocking (bool): Si True, la fonction attend un clic avant de continuer.
        """
        if not blocking:
            clic = self.view.recup_clic()
        elif blocking:
            clic = self.view.attend_clic()

        if clic:
            obstacle = self.model.grid[clic.y //
                                       self.view.size][clic.x // self.view.size]
            if obstacle:
                self._change_obstacle_color(obstacle, mode)
            elif blocking:
                self.change_obstacle_color_on_click(mode, True)

    def change_obstacle_color_if_ball_present(self, ball: Ball, mode=str) -> None:
        """
        Change la couleur de l'obstacle si une bille est présente sur celui-ci.

        Args:
            ball (Ball): La bille en interaction avec l'obstacle.
            mode (str): Le mode de changement de couleur de l'obstacle.
        """
        obstacle = self.model.grid[ball.y][ball.x]
        if obstacle:
            # Si la bille est en contact avec un obstacle, change la couleur
            self._change_obstacle_color(obstacle, mode)

    def ball_traverse_board(self, ball: Ball):
        """
        Fait traverser la grille à la bille.

        Args:
            ball (Ball): La bille à faire traverser à travers la grille.
        """
        x1, y1 = ball.x, ball.y
        ball.traverse_board(self.model.num_columns-1, self.model.num_rows-1)
        self.view.update_ball_position(
            ball.object_view, x1, y1, ball.x, ball.y)
        self.update_ball_direction(ball)

    def remove_ball(self, ball: Ball):
        """
        Supprime une bille de la grille et de l'interface graphique.

        Args:
            ball (Ball): La bille à supprimer.
        """
        self.view.remove_ball(ball.object_view, ball.direction_view)
        self.model.remove_ball(ball)

    def simulate_food_chain(self):
        """
        Simule la chaîne alimentaire entre les billes et les fait "manger" les unes par les autres.
        """
        for ball in list(self.model.balls):
            for other_ball in list(self.model.balls):
                if self._detect_collision(ball, other_ball):
                    # Verifie si l'animal doit etre mangé ou pas
                    if ((self.model.ball_animals.index(ball.animal) - 1) % len(self.model.ball_animals)) == self.model.ball_animals.index(other_ball.animal):
                        self.remove_ball(ball)

    def rebound_ball_at_collision(self):
        """
        Gère le rebond des billes lors des collisions.
        """
        pass

    # ------------------- Private Methods -------------------

    def _change_obstacle_color(self, obstacle: Obstacle, mode, add_mode=None) -> None:
        """
        Change la couleur d'un obstacle selon le mode spécifié.

        Args:
            obstacle (Obstacle): L'obstacle dont la couleur doit être modifiée.
            mode (str): Le mode de changement de couleur.
            add_mode (bool, optional): Si True, ajoute la couleur de l'obstacle actuel.
        """

        colors = list(self.model.obstacle_colors.keys())

        if add_mode:
            colors.append(obstacle.color)

        if obstacle.color in colors or add_mode:
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

    def _detect_collision(self, ball, other_ball):
        """
        Détecte si deux billes entrent en collision.

        Args:
            ball (Ball): La première bille.
            other_ball (Ball): La seconde bille.

        Returns:
            bool: True si les billes entrent en collision, sinon False.
        """
        dir = {
            "left": (-1, 0),
            "right": (1, 0),
            "up": (0, -1),
            "down": (0, 1)
        }

        if other_ball is not ball:

            if ball.x == other_ball.x and ball.y == other_ball.y:
                return True

            # Regarde unquement la case voisine qui est dans sa direction
            elif (ball.x + dir[ball.direction][0] + self.model.num_columns) % self.model.num_columns == other_ball.x:
                if (ball.y + dir[ball.direction][1] + self.model.num_rows) % self.model.num_rows == other_ball.y:
                    # Vérifie que l'animal voisin et la direction oposé de la sienne (va le traverser)
                    if self.model.ball_directions[(self.model.ball_directions.index(ball.direction) + 2) % 4] == other_ball.direction:
                        return True
