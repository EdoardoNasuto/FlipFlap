from random import choice, choices, shuffle

from src.models.grid_model import Grid
from src.views.game_view import GameView


class SetupController:
    """
    Gère les paramètres initiaux et la configuration du menu pour le jeu.

    Attributes:
        num_rows (int): Nombre de lignes dans la grille de jeu.
        num_columns (int): Nombre de colonnes dans la grille de jeu.
        num_obstacles (int): Nombre d'obstacles placés dans la grille.
        num_balls (int): Nombre de billes présentes dans le jeu.
        game_mode (str): Mode de jeu sélectionné, tel que 'base' ou 'trap'.
    """

    def __init__(self, num_rows: int, num_columns: int, num_obstacles: int, num_balls: int, size: int, game_mode: str):
        """
        Initialise les paramètres du menu.

        Args:
            num_rows (int): Nombre de lignes dans la grille de jeu.
            num_columns (int): Nombre de colonnes dans la grille de jeu.
            num_obstacles (int): Nombre d'obstacles placés dans la grille.
            num_balls (int): Nombre de billes présentes dans le jeu.
            game_mode (str): Mode de jeu sélectionné, tel que 'base' ou 'trap'.
        """
        self.num_rows = num_rows
        self.num_columns = num_columns
        self.num_obstacles = num_obstacles
        self.num_balls = num_balls
        self.size = size
        self.game_mode = game_mode
        self.setup()

    def setup(self):
        import src.rules.game_mode_rules as game_mode
        if self.game_mode == "trap":
            game_mode.trap_game_setup(self)
        elif self.game_mode == "base":
            game_mode.base_game_setup(self)
        elif self.game_mode == "poule renard vipere":
            game_mode.poule_renard_vipere_game_setup(self)

    def setup_model(self, random_obstacle: bool, random_balls: bool, animal: bool):
        self.model = Grid(self.num_rows, self.num_columns)
        coords_obstacle, coords_balls = self._setup_items_coords(
            random_obstacle, random_balls)
        self._setup_obstacles(self.num_obstacles, coords_obstacle)
        self._setup_balls(self.num_balls, coords_balls, animal)

    def _setup_items_coords(self, random_obstacle, random_balls):
        obstacles_coordinates, balls_coordinates = [], []
        self.available_coords = [(x, y) for x in range(self.num_columns)
                                 for y in range(self.num_rows)]

        if random_obstacle:
            obstacles_coordinates = choices(
                self.available_coords, k=self.num_obstacles)
            self.available_coords = [
                coord for coord in self.available_coords if coord not in obstacles_coordinates]

        elif not random_obstacle:
            obstacles_coordinates.extend(self.select_coordinates_equally(
                self.num_obstacles))

        if random_balls:
            balls_coordinates = choices(
                self.available_coords, k=self.num_balls)
            self.available_coords = [
                coord for coord in self.available_coords if coord not in balls_coordinates]

        elif not random_obstacle:
            balls_coordinates.extend(self.select_coordinates_equally(
                self.num_balls))

        shuffle(obstacles_coordinates), shuffle(balls_coordinates)
        return obstacles_coordinates, balls_coordinates

    def _setup_obstacles(self, n, coords):
        """
        Place un nombre défini d'obstacles dans la grille à des positions uniques.

        Args:
            n (int): Le nombre d'obstacles à ajouter.
            coords (list): Liste des coordonnées pour les obstacles.
        """
        weighted_colors = []
        for color, weight in self.model.obstacle_colors.items():
            # Calculer le nombre d'occurrences basées sur la fraction
            count = round(weight * n)
            weighted_colors.extend([color] * count)

        while len(weighted_colors) < self.num_obstacles:
            weighted_colors.append(
                choice(list(self.model.obstacle_colors.keys())))

        for i in range(n):
            color = weighted_colors[i]
            self.model.add_obstacle(coords[i][0], coords[i][1], color)

    def _setup_balls(self, n, coords, animal):
        """
        Place un nombre défini de billes dans la grille.

        Args:
            n (int): Le nombre de billes à ajouter.
            coords (list): Liste des coordonnées pour les billes.
        """
        for i in range(n):
            direction = self.model.ball_directions[i % len(
                self.model.ball_directions)]
            self.model.add_ball(
                coords[i][0], coords[i][1], direction,
                self.model.ball_animals[i % len(self.model.ball_animals)] if animal else ...)

    def select_coordinates_equally(self, n_items: int) -> list:
        """
        Sélectionne aléatoirement des coordonnées (x, y) dans une grille de manière à répartir
        les items aussi équitablement que possible entre les colonnes.

        Args :
        - n_items (int) : Le nombre total d'items à placer sur la grille.

        Return :
        - result (list) : Une liste de tuples (x, y) représentant les coordonnées sélectionnées.

        Attributs requis dans `self` :
        - self.num_rows (int) : Le nombre de lignes dans la grille.
        - self.num_columns (int) : Le nombre de colonnes dans la grille.
        - self.available_coords (list) : Une liste des coordonnées disponibles sous forme de tuples (x, y).

        Notes :
        - Les colonnes sont sélectionnées aléatoirement en excluant celles déjà utilisées.
        - Les coordonnées (x, y) sont sélectionnées aléatoirement parmi celles disponibles
        dans une colonne donnée.
        - Une réinitialisation temporaire de `available_y` est effectuée si toutes les lignes
        d'une colonne ont déjà été utilisées.
        """
        selected_coordinates = []
        used_x = []  # Liste des indices de colonnes déjà utilisées
        # Liste des indices de lignes disponibles
        available_y = [y for y in range(self.num_rows)]

        # Calcul du nombre d'items par colonne
        items_per_x = n_items // self.num_columns

        # Reste des items non répartis uniformément
        remaining_items = n_items % self.num_columns

        for index in range(self.num_columns):
            # Sélectionner une colonne x qui n'a pas encore été utilisée
            x = choice([x for x in range(self.num_columns) if x not in used_x])
            used_x.append(x)

            # Ajouter un item supplémentaire pour les premières colonnes si nécessaire
            if index < remaining_items:
                items_per_x += 1

            # Répartir les items dans la colonne sélectionnée
            for _ in range(items_per_x):

                # Si toutes les lignes de la colonne sont utilisées, réinitialiser available_y
                if len(available_y) == 0:
                    available_y = [y for y in range(self.num_rows)]

                # Trouver toutes les coordonnées disponibles dans la colonne x
                available_coords_in_x = [
                    coord for coord in self.available_coords if coord[0] == x and coord[1] in available_y]
                selected_coord = choice(available_coords_in_x)
                available_y.remove(selected_coord[1])
                self.available_coords.remove(selected_coord)
                selected_coordinates.append(selected_coord)

            # Réinitialiser items_for_x pour la prochaine colonne
            items_per_x = n_items // self.num_columns

        return selected_coordinates

    # -----------------------------------------------------

    def setup_view(self):
        self.view = GameView(self.num_rows, self.num_columns, self.size)
        self.setup_obstacles()
        self.setup_grid()
        self.setup_balls()

    def setup_obstacles(self):
        """
        Dessine tout les obstacles de la grille
        """
        for column in range(self.model.num_columns):
            for row in range(self.model.num_rows):
                obstacle = self.model.grid[row][column]
                if obstacle:
                    obstacle.object_view = self.view.draw_obstacle(
                        obstacle.x, obstacle.y, obstacle.color)

    def setup_grid(self) -> None:
        """
        Dessine les cases de la grille.
        """
        self.view.draw_grid(self.model.num_rows, self.model.num_columns)

    def setup_balls(self) -> None:
        """
        Dessine toutes les billes sur la grille.
        """
        for ball in self.model.balls:
            if not ball.animal:
                ball.object_view = self.view.draw_ball(ball)
            elif ball.animal:
                ball.object_view = self.view.draw_ball(
                    ball, f"assets/{ball.animal}.png")
