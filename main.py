from src.rules.game_mode_rules import *
from src.views.menu import *

GRID_NUM_ROWS = 10
GRID_NUM_COLUMNS = 10
NUM_OBSTACLES = 20
NUM_BALLS = 10
SIZE = 50
SPEED = 1
MODE = "trap"

CONFIG_MODE = False


def main():
    """
    Fonction principale pour initialiser et lancer l'application Flip/Flap.
    Cette fonction configure les composants du modèle, de la vue et du contrôleur,
    puis démarre la simulation.
    """
    if CONFIG_MODE:
        root = tk.Tk()
        Menu(root)
        root.mainloop()

    else:
        if MODE.lower() == "base":
            base_game(GRID_NUM_ROWS, GRID_NUM_COLUMNS,
                      NUM_OBSTACLES, NUM_BALLS, SIZE, SPEED)
        elif MODE.lower() == "trap":
            trap_game(GRID_NUM_ROWS, GRID_NUM_COLUMNS,
                      NUM_OBSTACLES, NUM_BALLS, SIZE, SPEED)
        elif MODE.lower() == "poule renard vipere":
            poule_renard_vipere_game(GRID_NUM_ROWS, GRID_NUM_COLUMNS,
                                     NUM_OBSTACLES, NUM_BALLS, SIZE, SPEED)


if __name__ == "__main__":
    main()
