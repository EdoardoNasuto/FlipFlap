from src.views.libs.tkiteasy import *
from typing import List


class GameView:
    """
    Cette classe gère l'affichage de la grille, des obstacles, et des billes dans une fenêtre graphique.

    Attributes:
        window (object): Fenêtre graphique pour l'affichage et les interactions utilisateur.
        height (int): Hauteur de la fenêtre en pixels.
        width (int): Largeur de la fenêtre en pixels.
        size (int): Taille d'une case de la grille en pixels.
    """

    def __init__(self, num_rows: int, num_columns: int, size: int):
        """
        Initialise la fenêtre de jeu avec une grille d'une taille spécifiée.

        Args:
            num_rows (int): Nombre de lignes de la grille.
            num_columns (int): Nombre de colonnes de la grille.
            size (int): Taille d'une case de la grille en pixels.
        """
        self.window = ouvrirFenetre(num_columns*size, num_rows*size)
        self.height = num_rows * size
        self.width = num_columns * size
        self.size = size

    def draw_grid(self, num_rows: int, num_columns: int) -> None:
        """
        Dessine une grille de lignes et de colonnes dans la fenêtre.

        Args:
            num_rows (int): Nombre de lignes.
            num_columns (int): Nombre de colonnes.
        """
        for x in range(num_columns):
            self.window.dessinerLigne(
                x*self.size, 0, x*self.size, self.height, "white")
        for y in range(num_rows):
            self.window.dessinerLigne(
                0, y*self.size, self.width, y*self.size, "white")

    def draw_obstacle(self, column: int, row: int, color: str) -> ObjetGraphique:
        """
        Dessine un obstacle à une position donnée sur la grille.

        Args:
            column (int): Colonne de l'obstacle.
            row (int): Ligne de l'obstacle.
            color (str): Couleur de l'obstacle.

        Returns:
            ObjetGraphique: L'objet graphique représentant l'obstacle dessiné.

        """
        return self.window.dessinerRectangle(
            column * self.size, row * self.size,
            self.size, self.size, color
        )

    def update_obstacle_color(self, obstacle: object, color: str):
        """
        Modifie la couleur d'un obstacle existant.

        Args:
            obstacle(object): L'objet représentant l'obstacle.
            color(str): La nouvelle couleur de l'obstacle.
        """
        self.window.changerCouleur(obstacle, color)

    def recup_clic(self):
        """
        Récupère le clic de l'utilisateur.

        Returns:
            tuple: La position du clic de l'utilisateur sous forme de coordonnées(x, y).
        """
        return self.window.recupererClic()

    def attend_clic(self):
        """
        Récupère le clic de l'utilisateur.

        Returns:
            tuple: La position du clic de l'utilisateur sous forme de coordonnées(x, y).
        """
        return self.window.attendreClic()

    def draw_ball(self, ball: object, file: str = None) -> ObjetGraphique:
        """
        Dessine une bille à sa position actuelle ou affiche une image.

        Args:
            ball (object): Bille à dessiner (attributs : `x`, `y`).
            file (Optional[str]): Chemin du fichier image à utiliser.

        Returns:
            ObjetGraphique: Représentation graphique de la bille.
        """
        if not file:
            r = self.size/2
            return self.window.dessinerDisque(ball.x*self.size+r, ball.y*self.size+r, r-1, "white")
        elif file:
            return self.window.afficherImage(ball.x*self.size, ball.y*self.size, file, self.size-1, self.size-1)

    def update_ball_position(self, ball: object, x1: int, y1: int, x2: int, y2: int) -> None:
        """
        Déplace une bille d'une position initiale à une nouvelle position.

        Args:
            ball (object): Bille à déplacer.
            x1 (int): Position X initiale.
            y1 (int): Position Y initiale.
            x2 (int): Nouvelle position X.
            y2 (int): Nouvelle position Y.
        """
        self.window.deplacer(ball, x2*self.size-x1 *
                             self.size, y2*self.size-y1*self.size)

    def update_ball_direction_arrow(self, ball: object) -> None:
        """
        Met à jour l'affichage de la flèche indiquant la direction de la bille.

        Args:
            ball (object): Bille avec sa direction et flèche à afficher.
        """
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

    def remove_ball(self, ball_object: object, ball_direction: List[object]) -> None:
        """
        Supprime une bille et sa flèche de direction.

        Args:
            ball_object (object): Bille à supprimer.
            ball_direction (List[object]): Flèche associée à la bille.
        """
        self.window.supprimer(ball_object)
        for line in ball_direction:
            self.window.supprimer(line)

    def refresh(self) -> None:
        """ Actualise l'affichage de la fenêtre graphique. """
        self.window.actualiser()

    def exit_game(self) -> None:
        """ Termine la simulation et ferme la fenêtre graphique après un clic de l'utilisateur. """
        self.window.attendreClic()
        self.window.fermerFenetre()

    def listbox_popup(self, elements: list):
        """
        Affiche une fenêtre de sélection de liste et retourne l'élément choisi.

        Args:
            elements (list): Liste des éléments à afficher.

        Returns:
            Optional[int]: Index de l'élément sélectionné, ou None si aucune sélection.
        """
        self.selected_index = None

        root = tk.Tk()
        root.title("Exemple Listbox")

        # Création de la Listbox
        listbox = tk.Listbox(root, height=10, width=30)
        listbox.pack(pady=20)

        # Ajout d'éléments à la Listbox
        for element in elements:
            listbox.insert(tk.END, element)

        def on_validate():
            selection = listbox.curselection()
            if selection:
                self.selected_index = selection[0]
            root.quit()  # Ferme la fenêtre après validation

        # Bouton de validation
        validate_button = tk.Button(root, text="Valider", command=on_validate)
        validate_button.pack(pady=10)

        root.mainloop()  # L'attente de l'utilisateur
        root.destroy()

        return self.selected_index
