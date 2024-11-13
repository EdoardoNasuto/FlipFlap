from src.controllers.game_controller import GameController
from src.models.grid_model import Grid
from src.views.game_view import GameView

GRID_WIDTH = 50
GRID_HEIGHT = 50
NUM_OBSTACLES = 100
NUM_BALLS = 1


def main():
    """
    Fonction principale pour initialiser et lancer l'application Flip/Flap.
    Cette fonction configure les composants du modèle, de la vue et du contrôleur,
    puis démarre la simulation.
    """
    grid = Grid(GRID_WIDTH, GRID_HEIGHT)
    gui = GameView(grid, 10)
    controller = GameController(grid, gui, NUM_OBSTACLES, NUM_BALLS)
    controller.start_round()


if __name__ == "__main__":
    main()
