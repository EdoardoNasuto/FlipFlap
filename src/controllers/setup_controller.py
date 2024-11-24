from random import sample

from src.models.grid_model import Grid
from src.views.game_view import GameView
import src.controllers.game_mode_controller as game_mode


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
        if self.game_mode == "trap":
            game_mode.trap_game_setup()
        self.setup_model()
        self.setup_view()

    def setup_model(self):
        self.model = Grid(self.num_rows, self.num_columns)
        coords = [(x, y) for x in range(self.num_columns)
                  for y in range(self.num_rows)]
        # fonction random qui permet de tirer au hasard à l'intérieur de cette liste un nbr n d'élément EX :
        # Si ya 100 obstacles il va piocher 100 coordonnées
        coords = sample(coords, self.num_obstacles+self.num_balls)
        self._setup_obstacles(self.num_obstacles, coords[:self.num_obstacles])
        self._setup_balls(self.num_balls, coords[self.num_obstacles:])

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
        for i in range(n):
            color = weighted_colors[i]
            self.model.add_obstacle(coords[i][0], coords[i][1], color)

    def _setup_balls(self, n, coords):
        """
        Place un nombre défini de billes dans la grille.

        Args:
            n (int): Le nombre de billes à ajouter.
            coords (list): Liste des coordonnées pour les billes.
        """
        for i in range(n):
            direction = self.model.ball_directions[i % len(
                self.model.ball_directions)]
            self.model.add_ball(coords[i][0], coords[i][1], direction)

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
            ball.object_view = self.view.draw_ball(ball)
