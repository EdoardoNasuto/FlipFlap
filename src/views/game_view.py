from src.views.libs.tkiteasy import *


class GameView:
    """Interface graphique pour afficher la simulation de la grille et gérer les interactions utilisateur.

    Attributes:
        window: La fenêtre graphique utilisée pour afficher la grille.
    """

    def __init__(self, grid: object, size):
        """
        Initialise l'interface graphique avec une grille et une taille de case spécifiée.

        Crée la fenêtre de la simulation en fonction des dimensions de la grille et attend un clic pour démarrer.

        Args:
            grid (object): La grille de la simulation, contenant les obstacles et les billes.
            size (int): La taille de chaque case de la grille, en pixels.
        """
        self.window = ouvrirFenetre(grid.width*size, grid.height*size)
        self.window.attendreClic()
        self.window.fermerFenetre()

    def create_grid(self):
        """
        Dessine les cases et crée les éléments graphiques.
        """
        ...

    def update_ball(self, x1: int, y1: int, x2: int, y2: int):
        """
        Déplace la bille de sa position actuelle `(x1, y1)` vers sa nouvelle position `(x2, y2)` dans la grille.

        Args:
            x1 (int): Coordonnée x de la position actuelle de la bille.
            y1 (int): Coordonnée y de la position actuelle de la bille.
            x2 (int): Coordonnée x de la nouvelle position de la bille.
            y2 (int): Coordonnée y de la nouvelle position de la bille.
        """
