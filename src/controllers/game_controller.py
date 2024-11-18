from src.views.game_view import GameView
from src.models.grid_model import Grid


class GameController:
    """
    Gère la logique de contrôle pour la simulation, incluant la grille, les obstacles, les billes et l'interface graphique.

    Attributes:
        model (Grid): La grille contenant les obstacles et les billes.
        view (GUI): L'interface graphique pour afficher la simulation.
    """

    def __init__(self, grid: Grid, gui: GameView):
        """
        Initialise le contrôleur avec une grille, une vue, et configure les obstacles et billes.

        Args:
            grid (Grid): L'instance de la grille utilisée pour la simulation.
            gui (GameView): L'interface graphique pour la simulation.
        """
        self.model = grid
        self.view = gui

    def start_round(self):
        """
        Lance un round de simulation dans laquelle les billes interagissent avec les obstacles et se déplacent sur la grille.
        """
        ...
