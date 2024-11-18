from src.views.libs.tkiteasy import *
from src.models.grid_model import Grid


class GameView:
    """Interface graphique pour afficher la simulation de la grille et gérer les interactions utilisateur.

    Attributes:
        window: La fenêtre graphique utilisée pour afficher la grille.
    """

    def __init__(self, grid: Grid, size):
        """
        Initialise l'interface graphique avec une grille et une taille de case spécifiée.

        Crée la fenêtre de la simulation en fonction des dimensions de la grille et attend un clic pour démarrer.

        Args:
            grid (object): La grille de la simulation, contenant les obstacles et les billes.
            size (int): La taille de chaque case de la grille, en pixels.
        """
        self.window = ouvrirFenetre(grid.columns*size, grid.lines*size)
        self.model = grid
        self.size = size
        self.create_grid()
        self.create_obstacle()
        self.create_balls()

    def create_grid(self) -> None:
        """
        Dessine les cases de la grille.
        """
        for x in range(0, self.model.columns):
            self.window.dessinerLigne(
                x*self.size, 0, x*self.size, self.model.lines*self.size,  "white")
        for y in range(0, self.model.lines):
            self.window.dessinerLigne(
                0, y*self.size, self.model.columns*self.size, y*self.size,  "white")

    def create_obstacle(self) -> None:
        """
        Dessine les obstacles sur la grille
        """
        for line in range(self.model.lines):
            for column in range(self.model.columns):
                if self.model.grid[line][column] != 0:
                    self.window.dessinerRectangle(
                        column*self.size+1, line*self.size+1, self.size-2, self.size-2,
                        self.model.grid[line][column].color)

    def create_balls(self) -> None:
        """
        Dessine les billes sur la grille
        """
        ...

    def update_ball(self, x1: int, y1: int, x2: int, y2: int) -> None:
        """
        Déplace la bille de sa position actuelle `(x1, y1)` vers sa nouvelle position `(x2, y2)` dans la grille.

        Args:
            x1 (int): Coordonnée x de la position actuelle de la bille.
            y1 (int): Coordonnée y de la position actuelle de la bille.
            x2 (int): Coordonnée x de la nouvelle position de la bille.
            y2 (int): Coordonnée y de la nouvelle position de la bille.
        """
        ...
