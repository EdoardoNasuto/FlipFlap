class Ball:
    """
    Représente une bille se déplaçant dans une grille.

    Attributes:
        available_directions (list): Les directions que la bille peut prendre.
        x (int): La position actuelle en x de la bille.
        y (int): La position actuelle en y de la bille.
        direction (str): La direction actuelle de la bille parmi 'available_directions'.
        object_view (Any): L'objet graphique représentant la bille.
    """
    available_directions = ["left", "up", "right", "down"]

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
        index = self.available_directions.index(self.direction)
        self.direction = self.available_directions[(index - 1) % 4]

    def turn_right(self) -> None:
        """Tourne la bille en direction de la droite."""
        index = self.available_directions.index(self.direction)
        self.direction = self.available_directions[(index + 1) % 4]

    def reverse(self) -> None:
        """Fait faire demi-tour à la direction bille."""
        index = self.available_directions.index(self.direction)
        self.direction = self.available_directions[(index + 2) % 4]
