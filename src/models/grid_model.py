from random import sample
from src.models.obstacle_model import Obstacle


class Grid:
    """
    Représente une grille de jeu avec des obstacles et des billes.

    Attributes:
        width (int): La largeur de la grille.
        height (int): La hauteur de la grille.
        grid (list): La matrice représentant la grille.
        balls (list): La liste des billes ajoutées à la grille.
    """

    def __init__(self, width: int, height: int, num_obstacles: int, num_balls: int):
        """
        Initialise une grille de jeu avec la largeur et la hauteur.

        Args:
            width (int): La largeur de la grille.
            height (int): La hauteur de la grille.
        """
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
        self.balls = []
        self.setup_obstacles(num_obstacles)
        self.setup_balls(num_balls)

    def setup_obstacles(self, n):
        """
        Ajoute un nombre défini d'obstacles dans la grille pour interagir avec les billes.

        Args:
            n (int): Le nombre d'obstacles à ajouter.
        """
        coord = []
        for x in range(self.height):
            for y in range(self.width):
                coord.append((x, y))
        coord = sample(coord, n)
        for i in range(n):
            self.add_obstacle(
                coord[i][0], coord[i][1], Obstacle(coord[0], coord[1], "red"))

    def setup_balls(self, n):
        """
        Place un nombre défini de billes dans la grille à une position aléatoire unique.

        Args:
            n (int): Le nombre de billes à ajouter.
        """
        ...

    def add_obstacle(self, x: int, y: int, obstacle: object) -> None:
        """
        Ajoute un obstacle à la grille à la position (x, y).

        Args:
            x (int): La position en x de l'obstacle.
            y (int): La position en y de l'obstacle.
            obstacle (object): L'obstacle à ajouter à la grille.
        """
        self.grid[x][y] = obstacle

    def add_ball(self, ball: object) -> None:
        """Ajoute une bille à la grille.

        Args:
            ball (object): La bille à ajouter à la grille.
        """
        self.balls.append(ball)

    def is_valid_position(self, x: int, y: int) -> bool:
        """Vérifie si la position (x, y) est valide (dans les limites de la grille).

        Args:
            x (int): La position en x.
            y (int): La position en y.

        Returns:
            bool: True si la position est valide, sinon False.
        """
        if 0 <= x < self.height and 0 <= y < self.width:
            return True
        return False

    def display(self) -> str:
        """ Affiche la grille avec les obstacles et billes pour le débogage. """
        for line in self.grid:
            print(line)
