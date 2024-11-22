from src.views.libs.tkiteasy import *
from src.models.grid_model import Grid


class GameView:
    """
    Cette classe gère l'affichage de la grille, des obstacles, et des billes dans une fenêtre graphique.

    Attributes:
        window (object): La fenêtre graphique utilisée pour afficher la grille et interagir avec l'utilisateur.
        model (Grid): L'objet représentant la grille, contenant les obstacles et les billes.
        size (int): La taille de chaque case de la grille, en pixels.
    """

    def __init__(self, grid: Grid, size: int):
        """
        Initialise l'interface graphique avec une grille et une taille de case spécifiée.

        Crée la fenêtre de la simulation en fonction des dimensions de la grille et attend un clic pour démarrer.

        Args:
            grid (Grid): La grille de la simulation, contenant les obstacles et les billes.
            size (int): La taille de chaque case de la grille, en pixels.
        """
        self.window = ouvrirFenetre(grid.num_columns*size, grid.num_rows*size)
        self.model = grid
        self.size = size
        self._create_grid()
        self._create_obstacles()
        self._create_balls()
        self.window.actualiser()

    def _create_grid(self) -> None:
        """
        Dessine les cases de la grille.
        """
        for x in range(0, self.model.num_columns):
            self.window.dessinerLigne(
                x*self.size, 0, x*self.size, self.model.num_rows*self.size,  "white")
        for y in range(0, self.model.num_rows):
            self.window.dessinerLigne(
                0, y*self.size, self.model.num_columns*self.size, y*self.size,  "white")

    def _create_obstacles(self) -> None:
        """ Dessine tout les obstacles de la grille """
        for column in range(self.model.num_columns):
            for row in range(self.model.num_rows):
                if self.model.grid[row][column]:
                    self._draw_obstacle(column, row)

    def _draw_obstacle(self, column: int, row: int) -> None:
        """
        Dessine un obstacle à une position donnée sur la grille.

        Args:
            column (int): La colonne où dessiner l'obstacle.
            row (int): La ligne où dessiner l'obstacle.
        """
        self.model.grid[row][column].object_view = self.window.dessinerRectangle(
            column * self.size + 1, row * self.size + 1,
            self.size - 1, self.size - 1,
            self.model.grid[row][column].color
        )

    def update_obstacle_color(self, obstacle: object, color: str):
        self.window.changerCouleur(obstacle, color)

    def _create_balls(self) -> None:
        """ Dessine toutes les billes sur la grille. """
        for ball in self.model.balls:
            self._draw_ball(ball)

    def _draw_ball(self, ball: object) -> None:
        """
        Dessine une bille sur la grille à sa position actuelle.

        Args:
            ball (object): L'objet représentant la bille à dessiner (attributs : `x`, `y`, `object_view`).
        """
        r = self.size/2
        ball.object_view = self.window.dessinerDisque(
            ball.x*self.size+r, ball.y*self.size+r, r-1, "white")

    def update_ball(self, ball: object, x1: int, y1: int, x2: int, y2: int) -> None:
        """
        Déplace la bille de sa position actuelle `(x1, y1)` vers sa nouvelle position `(x2, y2)` dans la grille.

        Args:
            ball (object): L'objet représentant la bille à déplacer.
            x1 (int): Coordonnée x de la position actuelle de la bille.
            y1 (int): Coordonnée y de la position actuelle de la bille.
            x2 (int): Coordonnée x de la nouvelle position de la bille.
            y2 (int): Coordonnée y de la nouvelle position de la bille.
        """
        self.window.deplacer(ball, x2*self.size-x1 *
                             self.size, y2*self.size-y1*self.size)

    def remove_ball(self, ball: object) -> None:
        """
        Supprime une bille de la grille.

        Args:
            ball (object): L'objet représentant la bille à supprimer (attributs : `x`, `y`, `object_view`).
        """
        self.window.supprimer(ball)

    def refresh(self) -> None:
        """ Actualise l'affichage de la fenêtre graphique."""
        self.window.actualiser()

    def exit_game(self) -> None:
        """ Termine la simulation et ferme la fenêtre graphique après un clic de l'utilisateur. """
        self.window.attendreClic()
        self.window.fermerFenetre()
