from src.controllers.game_controller import GameController
from src.views.game_view import GameView
from src.models.grid_model import Grid

GRID_NUM_ROWS = 10
GRID_NUM_COLUMNS = 10
NUM_OBSTACLES = 20
NUM_BALLS = 10
SIZE = 50


def main():
    """
    Fonction principale pour initialiser et lancer l'application Flip/Flap.
    Cette fonction configure les composants du modèle, de la vue et du contrôleur,
    puis démarre la simulation.
    """
    grid = Grid(GRID_NUM_ROWS, GRID_NUM_COLUMNS, NUM_OBSTACLES, NUM_BALLS)
    gui = GameView(GRID_NUM_ROWS, GRID_NUM_COLUMNS, SIZE)
    GameController(grid, gui, 1, "trap")


if __name__ == "__main__":
    main()
