from src.views.game_view import GameView
from src.models.grid_model import Grid
from src.models.obstacle_model import Obstacle
from random import sample


class GameController:
    """
    Gère la logique de contrôle pour la simulation, incluant la grille, les obstacles, les billes et l'interface graphique.

    Attributes:
        model (Grid): La grille contenant les obstacles et les billes.
        view (GUI): L'interface graphique pour afficher la simulation.
    """

    def __init__(self, grid: Grid, gui: GameView, num_obsctacles: int, num_balls: int):
        """
        Initialise le contrôleur avec une grille, une vue, et configure les obstacles et billes.

        Args:
            grid (Grid): L'instance de la grille utilisée pour la simulation.
            gui (GameView): L'interface graphique pour la simulation.
            num_obstacles (int): Le nombre d'obstacles à placer dans la grille.
            num_balls (int): Le nombre de billes à ajouter dans la grille.
        """
        self.model = grid
        self.view = gui
        self.setup_obstacles(num_obsctacles)
        self.setup_balls(num_balls)

    def setup_obstacles(self, n):
        """
        Ajoute un nombre défini d'obstacles dans la grille pour interagir avec les billes.

        Args:
            n (int): Le nombre d'obstacles à ajouter.
        """
        coord = []
        for x in range(self.model.grid):
            for y in range(self.model.grid[x]):
                coord.append((x, y))
        coord = sample(coord, n)
        for _ in range(n):
            self.model.add_obstacle(
                coord[0], coord[1], Obstacle(coord[0], coord[1], "red"))
        self.view.create_obstacle()

    def setup_balls(self, n):
        """
        Place un nombre défini de billes dans la grille pour démarrer la simulation.

        Args:
            n (int): Le nombre de billes à ajouter.
        """
        ...

    def start_round(self):
        """
        Lance un round de simulation dans laquelle les billes interagissent avec les obstacles et se déplacent sur la grille.
        """
        ...
