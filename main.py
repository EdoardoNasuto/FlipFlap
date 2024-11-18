from src.controllers.game_controller import GameController
from src.views.game_view import GameView
from src.models.grid_model import Grid

GRID_NUM_LINES = 50
GRID_NUM_COLUMNS = 50
NUM_OBSTACLES = 100
NUM_BALLS = 1
SIZE = 10


def main():
    """
    Fonction principale pour initialiser et lancer l'application Flip/Flap.
    Cette fonction configure les composants du modèle, de la vue et du contrôleur,
    puis démarre la simulation.
    """
    grid = Grid(GRID_NUM_LINES, GRID_NUM_COLUMNS, NUM_OBSTACLES, NUM_BALLS)
    gui = GameView(grid, SIZE)
    controller = GameController(grid, gui)
    gui.window.attendreClic()
    gui.window.fermerFenetre()


if __name__ == "__main__":
    main()
