class Ball:
    """
    Représente une bille se déplaçant dans une grille.

    Attributes:
        available_directions (list): Liste des directions possibles pour la bille.
        available_animals (list): Liste des animaux disponibles associés à la bille
        x (int): La position actuelle en x de la bille.
        y (int): La position actuelle en y de la bille.
        direction (str): La direction actuelle de la bille parmi 'available_directions'.
        animal (str): Type d'animal associé à la bille.
        object_view (Any): Représentation graphique de la bille (par défaut None).
        direction_view (Any): Représentation graphique de la direction de la bille (par défaut None).
    """
    available_directions = ["left", "up", "right", "down"]
    available_animals = ["poule", "renard", "vipere"]

    def __init__(self, x: int, y: int, direction: str, animal: str):
        """
        Initialise une bille avec une position initiale et une direction.

        Args:
            x (int): Position x initiale.
            y (int): Position y initiale.
            direction (str): Direction initiale.
            animal (str): Type d'animal associé à la bille.
        """
        self.x = x
        self.y = y
        self.direction = direction
        self.animal = animal
        self.object_view = None
        self.direction_view = None

    def move(self, test: bool = False) -> tuple[int, int] | None:
        """
        Déplace la bille en fonction de sa direction actuelle.

        Args:
            test (bool): Si True, retourne le déplacement sans modifier les coordonnées de la bille.

        Returns:
            tuple[int, int] | None: Les déplacements en X et Y si 'test' est True, sinon None.
        """
        moves = {
            "left": (-1, 0),
            "right": (1, 0),
            "up": (0, -1),
            "down": (0, 1)
        }
        dx, dy = moves[self.direction]
        if test:
            return dx, dy
        self.x += dx
        self.y += dy

    def traverse_board(self, max_x, max_y):
        """
        Permet à la bille de traverser le plateau en réapparaissant de l'autre côté.

        Args:
            max_x (int): Le valeur max de x sur la grille.
            max_y (int): Le valeur max de y sur la grille.
        """
        self.move()
        if not (0 <= self.x <= max_x):
            self.x = self.x % (max_x + 1)

        if not (0 <= self.y <= max_y):
            self.y = self.y % (max_y + 1)

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
