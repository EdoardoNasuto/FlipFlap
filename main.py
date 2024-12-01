from src.rules.game_mode_rules import *
from src.views.menu import *


def main():
    """
    Fonction principale pour initialiser et lancer l'application Flip/Flap.
    Cette fonction configure les composants du modèle, de la vue et du contrôleur,
    puis démarre la simulation.
    """
    root = tk.Tk()
    Menu(root)
    root.mainloop()


if __name__ == "__main__":
    main()
