from random import sample
from src.models.obstacle_model import Obstacle
from src.models.ball_model import Ball


class Grid:
    """
    Représente une grille de jeu avec des obstacles et des billes.

    Attributes:
        width (int): La largeur de la grille.
        height (int): La hauteur de la grille.
        grid (list): La matrice représentant la grille.
        balls (list): La liste des billes ajoutées à la grille.
    """

    def __init__(self, num_lines: int, num_columns: int, num_obstacles: int, num_balls: int):
        """
        Initialise une grille de jeu avec la largeur et la hauteur.

        Args:
            width (int): La largeur de la grille.
            height (int): La hauteur de la grille.
        """
        self.lines = num_lines
        self.columns = num_columns
        self.grid = [[0 for _ in range(self.columns)]
                     for _ in range(self.lines)]
        self.balls = []
        self.colors = ["red", "blue", "green"]
        self.direction = ["right", "left", "up", "down"]
        # appelle la fonction qui crée les obtacles
        self.setup_obstacles(n=num_obstacles)
        # appelle la fonction qui crée les balles
        self.setup_balls(n=num_balls)

    def setup_obstacles(self, n):
        """
        Ajoute un nombre défini d'obstacles dans la grille pour interagir avec les billes.

        Args:
            n (int): Le nombre d'obstacles à ajouter.
        """
        coord = []
        for x in range(self.columns):
            for y in range(self.lines):
                coord.append((x, y))
        # fonction random qui permet de tirer au hasard à l'intérieur de cette liste un nbr n d'élément EX : Si ya 100 obstacles il va piocher 100 coordonnées
        coord = sample(coord, n)
        for i in range(n):
            # permet d'avoir un meme nombre de carré pour chaque couleur
            color = self.colors[i % len(self.colors)]
            self.add_obstacle(coord[i][0], coord[i][1], color)

    def setup_balls(self, n):
        """
        Place un nombre défini de billes dans la grille à une position aléatoire unique.

        Args:
            n (int): Le nombre de billes à ajouter.
        """
        coord = []
        for x in range(self.columns):
            for y in range(self.lines):
                coord.append((x, y))
        coord = sample(coord, n)
        for i in range(n):
            direction = self.direction[i % len(self.direction)]
            self.add_ball(coord[i][0], coord[i][1], direction)

    def add_obstacle(self, x: int, y: int, color: str) -> None:
        """
        Ajoute un obstacle à la grille à la position (x, y).

        Args:
            x (int): La position en x de l'obstacle.
            y (int): La position en y de l'obstacle.
            color (str): La couleur de l'obstacle.
        """
        self.grid[y][x] = Obstacle(x, y, color)

    def add_ball(self, x: int,  y: int, direction: str) -> None:
        """Ajoute une bille à la grille.

        Args:
            ball (object): La bille à ajouter à la grille.
        """
        self.balls.append(Ball(x, y, direction))

    def is_valid_position(self, x: int, y: int) -> bool:
        """Vérifie si la position (x, y) est valide (dans les limites de la grille).

        Args:
            x (int): La position en x.
            y (int): La position en y.

        Returns:
            bool: True si la position est valide, sinon False.
        """
        if 0 <= x < self.columns and 0 <= y < self.lines:
            return True
        return False

    def display(self) -> str:
        """ Affiche la grille avec les obstacles et billes pour le débogage. """
        for line in self.grid:
            print(line)
