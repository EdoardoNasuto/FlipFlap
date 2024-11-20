class Ball:
    """
    Représente une bille se déplaçant dans une grille.

    Attributes:
        x (int): La position actuelle en x de la bille.
        y (int): La position actuelle en y de la bille.
        directions (list): Les directions valides que la bille peut prendre.
        direction (str): La direction actuelle de la bille parmi {directions}.
        object_view (Any): L'objet graphique représentant la bille.
    """
    directions = ["left", "up", "right", "down"]

    def __init__(self, x: int, y: int, direction: str):
        """
        Initialise une bille avec une position initiale et une direction.

        Args:
            x (int): Position x initiale.
            y (int): Position y initiale.
            direction (str): Direction initiale.
        """
        self.x = x
        self.y = y
        self.direction = direction
        self.object_view = None

    def move(self) -> None:
        """Déplace la bille en fonction de sa direction."""
        moves = {
            "left": (-1, 0),
            "right": (1, 0),
            "up": (0, -1),
            "down": (0, 1)
        }
        dx, dy = moves[self.direction]
        self.x += dx
        self.y += dy

    def turn_left(self) -> None:
        """Tourne la bille en direction de la gauche."""
        index = self.directions.index(self.direction)
        self.direction = self.directions[(index - 1) % 4]

    def turn_right(self) -> None:
        """Tourne la bille en direction de la droite."""
        index = self.directions.index(self.direction)
        self.direction = self.directions[(index + 1) % 4]

    def reverse(self) -> None:
        """Fait faire demi-tour à la direction bille."""
        index = self.directions.index(self.direction)
        self.direction = self.directions[(index + 2) % 4]
