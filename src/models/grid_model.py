from typing import Optional, List

from src.models.ball_model import Ball
from src.models.obstacle_model import Obstacle


class Grid:
    """
    Représente une grille de jeu contenant des obstacles et des billes. La grille est une matrice rectangulaire
    où chaque case peut contenir un obstacle ou être vide. Les billes se déplacent selon des directions définies
    dans la grille et interagissent avec les obstacles.

    Attributes:
        num_rows (int): Le nombre de lignes (hauteur) de la grille.
        num_columns (int): Le nombre de colonnes (largeur) de la grille.
        grid (List[List[Optional[Obstacle]]]): La matrice représentant la grille, où chaque case contient 
            soit un obstacle, soit `None` si elle est vide.
        balls (List[Ball]): La liste des billes présentes dans la grille, avec leurs positions et directions.
        obstacle_colors (List[str]): Liste des couleurs disponibles pour les obstacles, héritée de `Obstacle`.
        ball_directions (List[str]): Liste des directions possibles pour les billes, héritée de `Ball`.
    """

    def __init__(self, num_rows: int, num_columns: int):
        """
        Initialise une grille de jeu avec un certain nombre de lignes, colonnes, obstacles, et billes.

        Args:
            num_rows (int): Le nombre de lignes (hauteur) de la grille.
            num_columns (int): Le nombre de colonnes (largeur) de la grille.
            num_obstacles (int): Le nombre d'obstacles à placer dans la grille.
            num_balls (int): Le nombre de billes à placer dans la grille.
        """
        self.num_rows = num_rows
        self.num_columns = num_columns
        self.grid: List[List[Optional[Obstacle]]] = [[None for _ in range(self.num_columns)]
                                                     for _ in range(self.num_rows)]
        self.balls: List[Ball] = []
        self.obstacle_colors = Obstacle.available_colors
        self.ball_directions = Ball.available_directions

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
        """
        Ajoute une bille à la grille.

        Args:
            x (int): La position en x de la bille.
            y (int): La position en y de la bille.
            direction (str): la direction de la bille.
        """
        self.balls.append(Ball(x, y, direction))

    def remove_ball(self, ball):
        """
        Supprime une bille de la grille.

        Args:
            ball: L'objet représentant la bille à supprimer.
        """
        self.balls.remove(ball)

    def is_valid_position(self, x: int, y: int) -> bool:
        """
        Vérifie si la position(x, y) est valide(dans les limites de la grille).

        Args:
            x(int): La position en x.
            y(int): La position en y.

        Returns:
            bool: True si la position est valide, sinon False.
        """
        return 0 <= x < self.num_columns and 0 <= y < self.num_rows

    def display(self) -> str:
        """
        Affiche la grille avec les obstacles et billes pour le débogage.
        """
        for row in self.grid:
            for element in row:
                if element:
                    print(str(element.color).center(10), end="|")
                else:
                    print("".center(10), end="|")
            print(), print("-"*11*len(row))
