from src.views.libs.tkiteasy import *


class GameView:
    """
    Cette classe gère l'affichage de la grille, des obstacles, et des billes dans une fenêtre graphique.

    Attributes:
        window (object): La fenêtre graphique utilisée pour afficher la grille et interagir avec l'utilisateur.
        model (Grid): L'objet représentant la grille, contenant les obstacles et les billes.
        size (int): La taille de chaque case de la grille, en pixels.
    """

    def __init__(self, num_rows: int, num_columns: int, size: int):
        """
        Initialise l'interface graphique avec une grille et une taille de case spécifiée.

        Crée la fenêtre de la simulation en fonction des dimensions de la grille et attend un clic pour démarrer.

        Args:
            num_rows (int): Le nombre de lignes de la grille.
            num_columns (int): Le nombre de colonnes de la grille.
            size (int): La taille de chaque case de la grille, en pixels.
        """
        self.window = ouvrirFenetre(num_columns*size, num_rows*size)
        self.height = num_rows * size
        self.width = num_columns * size
        self.size = size

    def draw_grid(self, num_rows: int, num_columns: int) -> None:
        """
        Dessine les cases de la grille.

        Args:
            num_rows (int): Le nombre de lignes de la grille.
            num_columns (int): Le nombre de colonnes de la grille.
        """
        for x in range(num_columns):
            self.window.dessinerLigne(
                x*self.size, 0, x*self.size, self.height, "white")
        for y in range(num_rows):
            self.window.dessinerLigne(
                0, y*self.size, self.width, y*self.size, "white")

    def draw_obstacle(self, column: int, row: int, color: str) -> None:
        """
        Dessine un obstacle à une position donnée sur la grille.

        Args:
            column (int): La colonne où dessiner l'obstacle.
            row (int): La ligne où dessiner l'obstacle.
            color (str): La couleur de l'obstacle à dessiner.
        """
        return self.window.dessinerRectangle(
            column * self.size, row * self.size,
            self.size, self.size, color
        )

    def update_obstacle_color(self, obstacle: object, color: str):
        """
        Met à jour la couleur d'un obstacle.

        Args:
            obstacle (object): L'objet représentant l'obstacle.
            color (str): La nouvelle couleur de l'obstacle.
        """
        self.window.changerCouleur(obstacle, color)

    def recup_clic(self):
        """
        Récupère le clic de l'utilisateur.

        Returns:
            tuple: La position du clic de l'utilisateur sous forme de coordonnées (x, y).
        """
        return self.window.recupererClic()

    def draw_ball(self, ball: object, file: str = None) -> object:
        """
        Dessine une bille sur la grille à sa position actuelle.

        Args:
            ball (object): L'objet représentant la bille à dessiner (attributs : `x`, `y`, `object_view`).

        Returns:
            object: L'objet graphique représentant la bille (généré par `self.window.dessinerDisque`).
        """
        if not file:
            r = self.size/2
            return self.window.dessinerDisque(ball.x*self.size+r, ball.y*self.size+r, r-1, "white")
        elif file:
            return self.window.afficherImage(ball.x*self.size, ball.y*self.size, file, self.size-1, self.size-1)

    def update_ball_position(self, ball: object, x1: int, y1: int, x2: int, y2: int) -> None:
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

    def update_ball_direction(self, ball: object):
        if ball.direction_view:
            for line in ball.direction_view:
                self.window.supprimer(line)

        direction = {
            "left": (-1, 0),
            "right": (1, 0),
            "up": (0, -1),
            "down": (0, 1)
        }

        dir_x, dir_y = direction[ball.direction]

        # Calcul des coordonnées centrées dans la case
        center_x = ball.x * self.size + self.size / 2
        center_y = ball.y * self.size + self.size / 2
        offset = self.size / 4  # Décalage pour que la flèche reste dans la case

        start_x = center_x - dir_x * offset
        start_y = center_y - dir_y * offset
        end_x = center_x + dir_x * offset
        end_y = center_y + dir_y * offset

        # Dessiner la flèche
        ball.direction_view = self.window.dessinerFleche(
            start_x, start_y, end_x, end_y, self.size / 8, "red", 4)

    def remove_ball(self, ball_object: object, ball_direction: object) -> None:
        """
        Supprime une bille de la grille.

        Args:
            ball (object): L'objet représentant la bille à supprimer (attributs : `x`, `y`, `object_view`).
        """
        self.window.supprimer(ball_object)
        for line in ball_direction:
            self.window.supprimer(line)

    def refresh(self) -> None:
        """
        Actualise l'affichage de la fenêtre graphique.
        """
        self.window.actualiser()

    def exit_game(self) -> None:
        """
        Termine la simulation et ferme la fenêtre graphique après un clic de l'utilisateur.
        """
        self.window.attendreClic()
        self.window.fermerFenetre()
