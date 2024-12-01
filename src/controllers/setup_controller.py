from random import choice, sample, shuffle

from src.models.grid_model import Grid
from src.views.game_view import GameView
from src.rules.params_rule import *


class SetupController:
    """
    Gère les paramètres initiaux et la configuration de la grille pour le jeu.

    Attributes:
        num_rows (int): Nombre de lignes dans la grille de jeu.
        num_columns (int): Nombre de colonnes dans la grille de jeu.
        num_obstacles (int): Nombre d'obstacles placés dans la grille.
        num_balls (int): Nombre de billes présentes dans le jeu.
    """

    def __init__(self, num_rows: int, num_columns: int, num_obstacles: int, num_balls: int, size: int):
        """
        Initialise les paramètres de la grille

        Args:
            num_rows (int): Nombre de lignes dans la grille de jeu.
            num_columns (int): Nombre de colonnes dans la grille de jeu.
            num_obstacles (int): Nombre d'obstacles placés dans la grille.
            num_balls (int): Nombre de billes présentes dans le jeu.
        """
        self.num_rows = num_rows
        self.num_columns = num_columns
        self.num_obstacles = num_obstacles
        self.num_balls = num_balls
        self.size = size

    # ------------------- Public Methods -------------------

    def setup_model(self, random_obstacle: ItemSetup, random_balls: ItemSetup, ball_item: ItemnType, json_filename: str = None) -> None:
        """
        Configure le modèle de jeu en initialisant la grille, les obstacles et les billes.

        Args:
            random_obstacle (ItemSetup): La méthode de placement des obstacles (EQUALLY ou RANDOM).
            random_balls (ItemSetup): La méthode de placement des billes (EQUALLY ou RANDOM).
            ball_item (ItemnType): Le type d'élément à associer aux billes (par exemple, animaux).
        """
        if json_filename:
            self.import_from_json(json_filename)
        else:
            self.model = Grid(self.num_rows, self.num_columns)
            coords_obstacle, coords_balls = self._setup_items_coords(
                random_obstacle, random_balls)
            self._setup_obstacles(self.num_obstacles, coords_obstacle)
            self._setup_balls(self.num_balls, coords_balls, ball_item)

    def setup_view(self) -> None:
        """
        Configure la vue du jeu, dessinant la grille, les obstacles et les billes.

        Cette méthode initialise les éléments visuels du jeu sur la vue.
        """
        self.view = GameView(self.num_rows, self.num_columns, self.size)
        self.setup_obstacles()
        self.setup_grid()
        self.setup_balls()

    # ------------------- Private Methods -------------------

    def _setup_items_coords(self, random_obstacle: ItemSetup, random_balls: ItemSetup) -> list:
        """
        Détermine les coordonnées des obstacles et des billes en fonction de la méthode de placement.

        Args:
            random_obstacle (ItemSetup): Méthode pour le placement des obstacles.
            random_balls (ItemSetup): Méthode pour le placement des billes.

        Returns:
            tuple: Deux listes de coordonnées, une pour les obstacles et une pour les billes.
        """
        obstacles_coordinates, balls_coordinates = [], []
        self.available_coords = [(x, y) for x in range(self.num_columns)
                                 for y in range(self.num_rows)]

        if random_obstacle == ItemSetup.EQUALLY:
            obstacles_coordinates.extend(self._select_coordinates_equally(
                self.num_obstacles))

        if random_balls == ItemSetup.EQUALLY:
            balls_coordinates.extend(self._select_coordinates_equally(
                self.num_balls))

        if random_obstacle == ItemSetup.RANDOM:
            obstacles_coordinates = sample(
                self.available_coords, k=self.num_obstacles)
            self.available_coords = [
                coord for coord in self.available_coords if coord not in obstacles_coordinates]

        if random_balls == ItemSetup.RANDOM:
            balls_coordinates = sample(
                self.available_coords, k=self.num_balls)
            self.available_coords = [
                coord for coord in self.available_coords if coord not in balls_coordinates]

        shuffle(obstacles_coordinates), shuffle(balls_coordinates)
        return obstacles_coordinates, balls_coordinates

    def _setup_obstacles(self, n: int, coords: list) -> None:
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

    def _setup_balls(self, n: int, coords: list, item: ItemnType):
        """
        Place un nombre défini de billes dans la grille.

        Args:
            n (int): Le nombre de billes à ajouter.
            coords (list): Liste des coordonnées pour les billes.
            item (ItemType): Type de billes.
        """
        for i in range(n):
            direction = choice(self.model.ball_directions)
            self.model.add_ball(
                coords[i][0], coords[i][1], direction,
                self.model.ball_animals[i % len(self.model.ball_animals)] if item == ItemnType.ANIMALS else None)

    def _select_coordinates_equally(self, n_items: int) -> list:
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
                self.view.update_ball_direction_arrow(ball)
            elif ball.animal:
                ball.object_view = self.view.draw_ball(
                    ball, f"assets/{ball.animal}.png")
                self.view.update_ball_direction_arrow(ball)

    # -------------
    def export_to_json(self, filename: str) -> None:
        import json
        """
        Exporte les données du modèle (grille, obstacles, billes) au format JSON.

        Args:
            filename (str): Le nom du fichier où les données seront sauvegardées.
        """
        data = {
            'num_rows': self.num_rows,
            'num_columns': self.num_columns,
            'num_obstacles': self.num_obstacles,
            'num_balls': self.num_balls,
            'size': self.size,
            'grid': self._export_grid(),
            'obstacles': self._export_obstacles(),
            'balls': self._export_balls(),
        }

        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    def _export_grid(self) -> list:
        """
        Exporte les données de la grille (les coordonnées de chaque case) au format liste.

        Returns:
            list: Liste des coordonnées de la grille.
        """
        return [[(x, y) for x in range(self.num_columns)] for y in range(self.num_rows)]

    def _export_obstacles(self) -> list:
        """
        Exporte les obstacles présents dans la grille.

        Returns:
            list: Liste des obstacles avec leurs coordonnées et couleurs.
        """
        obstacles = []
        for column in range(self.model.num_columns):
            for row in range(self.model.num_rows):
                obstacle = self.model.grid[row][column]
                if obstacle:
                    obstacles.append({
                        'x': obstacle.x,
                        'y': obstacle.y,
                        'color': obstacle.color
                    })
        return obstacles

    def _export_balls(self) -> list:
        """
        Exporte les billes présentes dans la grille.

        Returns:
            list: Liste des billes avec leurs coordonnées et direction.
        """
        balls = []
        for ball in self.model.balls:
            balls.append({
                'x': ball.x,
                'y': ball.y,
                'direction': ball.direction,
                'animal': ball.animal
            })
        return balls

    def import_from_json(self, filename) -> None:
        import json
        """
        Importe les données du jeu depuis un fichier JSON et initialise la grille, les obstacles et les billes.

        Cette méthode charge les données du fichier JSON et les utilise pour configurer le jeu.
        """
        try:
            with open(filename, 'r') as file:
                data = json.load(file)

            self.num_rows = data.get('num_rows', self.num_rows)
            self.num_columns = data.get('num_columns', self.num_columns)
            self.num_obstacles = data.get('num_obstacles', self.num_obstacles)
            self.num_balls = data.get('num_balls', self.num_balls)
            self.size = data.get('size', self.size)

            # Recréer le modèle de la grille
            self.model = Grid(self.num_rows, self.num_columns)

            # Importer les obstacles
            for obstacle_data in data.get('obstacles', []):
                self.model.add_obstacle(
                    obstacle_data['x'], obstacle_data['y'], obstacle_data['color'])

            # Importer les billes
            for ball_data in data.get('balls', []):
                self.model.add_ball(
                    ball_data['x'], ball_data['y'], ball_data['direction'], ball_data.get('animal'))

        except FileNotFoundError:
            print(f"Le fichier {self.json_filename} n'a pas été trouvé.")
        except json.JSONDecodeError:
            print(
                f"Erreur de décodage JSON dans le fichier {self.json_filename}.")
