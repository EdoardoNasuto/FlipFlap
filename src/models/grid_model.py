from random import sample

from src.models.ball_model import Ball
from src.models.obstacle_model import Obstacle


class Grid:
    """
    Représente une grille de jeu avec des obstacles et des billes.

    Attributes:
        num_rows (int): Le nombre de lignes (hauteur) de la grille.
        num_columns (int): Le nombre de colonnes (largeur) de la grille.
        grid (list): La matrice représentant la grille, chaque case peut contenir un obstacle ou être vide.
        balls (list): La liste des billes présentes dans la grille.
        obstacle_colors (list): Liste des couleurs possibles des obstacles.
        available_directions (list): Liste des directions possibles des billes.
    """

    def __init__(self, num_rows: int, num_columns: int, num_obstacles: int, num_balls: int):
        """
        Initialise une grille de jeu avec la largeur et la hauteur, en ajoutant des obstacles et des billes.

        Args:
            num_rows (int): Le nombre de lignes (hauteur) de la grille.
            num_columns (int): Le nombre de colonnes (largeur) de la grille.
            num_obstacles (int): Le nombre d'obstacles à placer dans la grille.
            num_balls (int): Le nombre de billes à placer dans la grille.
        """
        self.num_rows = num_rows
        self.num_columns = num_columns
        self.grid = [[None for _ in range(self.num_columns)]
                     for _ in range(self.num_rows)]
        self.balls = []
        self.obstacle_colors = Obstacle.available_colors
        self.ball_directions = Ball.available_directions
        self.setup_obstacles(n=num_obstacles)
        self.setup_balls(n=num_balls)

    def setup_obstacles(self, n):
        """
        Ajoute un nombre défini d'obstacles dans la grille pour interagir avec les billes.

        Args:
            n (int): Le nombre d'obstacles à ajouter.
        """
        coord = []
        for x in range(self.num_columns):
            for y in range(self.num_rows):
                coord.append((x, y))
        # fonction random qui permet de tirer au hasard à l'intérieur de cette liste un nbr n d'élément EX : Si ya 100 obstacles il va piocher 100 coordonnées
        coord = sample(coord, n)
        for i in range(n):
            # permet d'avoir un meme nombre de carré pour chaque couleur
            color = self.obstacle_colors[i % len(self.obstacle_colors)]
            self.add_obstacle(coord[i][0], coord[i][1], color)

    def setup_balls(self, n):
        """
        Place un nombre défini de billes dans la grille à une position aléatoire unique.

        Args:
            n (int): Le nombre de billes à ajouter.
        """
        coord = []
        for x in range(self.num_columns):
            for y in range(self.num_rows):
                coord.append((x, y))
        coord = sample(coord, n)
        for i in range(n):
            direction = self.ball_directions[i % len(
                self.ball_directions)]
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
        if 0 <= x < self.num_columns and 0 <= y < self.num_rows:
            return True
        return False

    def display(self) -> str:
        """ Affiche la grille avec les obstacles et billes pour le débogage. """
        for line in self.grid:
            print(line)
