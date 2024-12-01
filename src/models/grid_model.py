from typing import Optional, List

from src.models.ball_model import Ball
from src.models.obstacle_model import Obstacle


class Grid:
    """
    Représente une grille de jeu contenant des obstacles et des billes. La grille est une matrice rectangulaire
    où chaque case peut contenir un obstacle ou être vide. Les billes se déplacent selon des directions définies
    dans la grille et interagissent avec les obstacles.

    Attributes:
        num_rows (int): Nombre de lignes (hauteur) de la grille.
        num_columns (int): Nombre de colonnes (largeur) de la grille.
        grid (List[List[Optional[Obstacle]]]): Matrice représentant la grille, où chaque case contient 
            soit un obstacle, soit `None` si elle est vide.
        balls (List[Ball]): Liste des billes présentes dans la grille, avec leurs positions et directions.
        obstacle_colors (dict): Dictionnaire des couleurs disponibles pour les obstacles, héritées de `Obstacle`.
        ball_directions (List[str]): Liste des directions possibles pour les billes, héritées de `Ball`.
        ball_animals (List[str]): Liste des animaux associés aux billes, héritée de `Ball`.
    """

    def __init__(self, num_rows: int, num_columns: int):
        """
        Initialise une grille de jeu avec un certain nombre de lignes et de colonnes.

        Args:
            num_rows (int): Nombre de lignes de la grille.
            num_columns (int): Nombre de colonnes de la grille.
        """
        self.num_rows = num_rows
        self.num_columns = num_columns
        self.grid: List[List[Optional[Obstacle]]] = [[None for _ in range(self.num_columns)]
                                                     for _ in range(self.num_rows)]
        self.balls: List[Ball] = []
        self.obstacle_colors = Obstacle.available_colors
        self.ball_directions = Ball.available_directions
        self.ball_animals = Ball.available_animals

    def add_obstacle(self, x: int, y: int, color: str) -> Obstacle:
        """
        Ajoute un obstacle à la grille à la position (x, y).

        Args:
            x (int): Position X de l'obstacle.
            y (int): Position Y de l'obstacle.
            color (str): Couleur de l'obstacle.

        Returns:
            Obstacle: L'obstacle ajouté.
        """
        self.grid[y][x] = Obstacle(x, y, color)
        return self.grid[y][x]

    def add_ball(self, x: int,  y: int, direction: str, animal: str = None) -> None:
        """
        Ajoute une bille à la grille à la position (x, y).

        Args:
            x (int): Position X de la bille.
            y (int): Position Y de la bille.
            direction (str): Direction initiale de la bille ('left', 'right', 'up', 'down').
            animal (str): Type d'animal associé à la bille. Par défaut, None.

        Returns:
            Ball: La bille ajoutée.
        """
        ball = Ball(x, y, direction, animal)
        self.balls.append(ball)
        return ball

    def remove_ball(self, ball) -> None:
        """
        Supprime une bille de la grille.

        Args:
            ball: L'objet représentant la bille à supprimer.
        """
        self.balls.remove(ball)

    def is_valid_position(self, x: int, y: int) -> bool:
        """
        Vérifie si la position (x, y) est dans les limites de la grille.

        Args:
            x (int): Position X
            y (int): Position Y

        Returns:
            bool: True si la position est valide, sinon False.
        """
        return 0 <= x < self.num_columns and 0 <= y < self.num_rows
