class Obstacle:
    """
    Représente un obstacle sur la grille qui peut affecter les billes.

    Attributes:
        x (int): La position en x de l'obstacle.
        y (int): La position en y de l'obstacle.
        color (str): La couleur de l'obstacle, déterminant son effet sur les billes.
    """

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

    def affect_ball(self, ball: object) -> None:
        """
        Applique l'effet de l'obstacle sur la bille en fonction de la couleur de l'obstacle.

        Args:
            ball (Ball): La bille sur laquelle l'obstacle aura un effet.
        """
        ...
