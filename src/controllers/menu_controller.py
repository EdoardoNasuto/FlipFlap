from src.views.game_view import GameView
from src.models.grid_model import Grid
import src.controllers.game_mode_controller as game_mode


class MenuController:
    """
    Gère les paramètres initiaux et la configuration du menu pour le jeu.

    Attributes:
        num_rows (int): Nombre de lignes dans la grille de jeu.
        num_columns (int): Nombre de colonnes dans la grille de jeu.
        num_obstacles (int): Nombre d'obstacles placés dans la grille.
        num_balls (int): Nombre de billes présentes dans le jeu.
        game_mode (str): Mode de jeu sélectionné, tel que 'base' ou 'trap'.
    """

    def __init__(self, num_rows: int, num_columns: int, num_obstacles: int, num_balls: int, game_mode: str):
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
        self.game_mode = game_mode
        self.setup()

    def setup(self):
        if self.game_mode == "trap":
            game_mode.trap_game_setup()

    def get_grid(self):
        return Grid(self.num_rows, self.num_columns,
                    self.num_obstacles, self.num_balls)
