from src.models.ball_model import Ball


class Obstacle:
    """
    Représente un obstacle sur la grille qui peut affecter les billes en modifiant leur trajectoire.

    Attributes:
        available_colors (list): Les couleurs que l'obstacle peut prendre par défault.
        x (int): La position en x de l'obstacle.
        y (int): La position en y de l'obstacle.
        color (str): La couleur de l'obstacle, déterminant son effet sur les billes.
        object_view (Any): L'objet graphique représentant l'obstacle.
    """
    available_colors = {"red": 0.50, "blue": 0.30, "green": 0.20}

    def __init__(self, x: int, y: int, color: str):
        """
        Initialise un obstacle à la position (x, y) avec une couleur spécifiée.

        Args:
            x (int): La position en x de l'obstacle.
            y (int): La position en y de l'obstacle.
            color (str): La couleur de l'obstacle qui détermine son effet sur la bille
        """
        self.x = x
        self.y = y
        self.color = color
        self.object_view = None

    def affect_ball(self, ball: Ball) -> str | None:
        """
        Applique l'effet de l'obstacle sur la bille en fonction de la couleur de l'obstacle.

        Args:
            ball (Ball): Bille sur laquelle l'obstacle a un effet.

        Returns:
            str | None: Une action spécifique si la couleur est "white" ou "purple", sinon None.
            - "delete": Supprime la bille.
            - "new_ball": Crée une nouvelle bille.
        """
        if self.color == "blue":
            ball.turn_right()

        elif self.color == "red":
            ball.turn_left()

        elif self.color == "green":
            ball.reverse()

        elif self.color == "white":
            return "delete"

        elif self.color == "purple":
            return "new_ball"
