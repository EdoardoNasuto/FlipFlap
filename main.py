from src.controllers.game_controller import GameController
from src.controllers.setup_controller import SetupController

GRID_NUM_ROWS = 10
GRID_NUM_COLUMNS = 10
NUM_OBSTACLES = 20
NUM_BALLS = 10
SIZE = 50
MODE = "poule renard vipere"


def main():
    """
    Fonction principale pour initialiser et lancer l'application Flip/Flap.
    Cette fonction configure les composants du modèle, de la vue et du contrôleur,
    puis démarre la simulation.
    """
    setup = SetupController(GRID_NUM_ROWS, GRID_NUM_COLUMNS,
                            NUM_OBSTACLES, NUM_BALLS, SIZE, MODE)
    GameController(setup.model, setup.view, 1, MODE)


if __name__ == "__main__":
    main()
