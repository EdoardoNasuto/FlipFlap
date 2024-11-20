class Ball:
    """
    Représente une bille se déplaçant dans une grille.

    Attributes:
        x (int): La position en x de la bille
        y (int): La position en y de la bille
        direction (str): La direction de la bille
    """

    def __init__(self, x: int, y: int, direction: str):
        """
        Initialise une bille à la position (x, y) avec une direction spécifiée.

        Attributes:
            x (int): La position en x de la bille
            y (int): La position en y de la bille
            direction (str): La direction de la bille
        """
        self.x = x
        self.y = y
        self.direction = direction
        self.object_view = None

    def move(self) -> None:
        """Déplace la bille en fonction de sa direction."""
        if self.direction == "left":
            self.x += -1
        if self.direction == "right":
            self.x += 1
        if self.direction == "up":
            self.y += -1
        if self.direction == "down":
            self.y += 1

    def turn_left(self) -> None:
        """Tourne la bille en direction de la gauche."""
        if self.direction == "left":
            self.direction = "down"
        elif self.direction == "right":
            self.direction = "up"
        elif self.direction == "up":
            self.direction = "left"
        elif self.direction == "down":
            self.direction = "right"

    def turn_right(self) -> None:
        """Tourne la bille en direction la droite."""
        if self.direction == "left":
            self.direction = "up"
        elif self.direction == "right":
            self.direction = "down"
        elif self.direction == "up":
            self.direction = "right"
        elif self.direction == "down":
            self.direction = "left"

    def reverse(self) -> None:
        """Fait faire demi-tour à la direction bille"""
        if self.direction == "left":
            self.direction = "right"
        elif self.direction == "right":
            self.direction = "left"
        elif self.direction == "up":
            self.direction = "down"
        elif self.direction == "down":
            self.direction = "down"
