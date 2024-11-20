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
        self.start_game()

    def start_game(self):
        from time import sleep
        print(len(self.model.balls))
        while len(self.model.balls) > 0:
            print(len(self.model.balls))
            sleep(1)
            self.run_round()
            self.view.window.actualiser()
        self.view.window.attendreClic()
        self.view.window.fermerFenetre()

    def run_round(self):
        """
        Lance un round de simulation dans laquelle les billes interagissent avec les obstacles et se déplacent sur la grille.
        """
        balls = list(self.model.balls)  # Prendre la liste et pas la variable
        for ball in balls:
            x1, y1 = ball.x, ball.y
            ball.move()
            if self.model.is_valid_position(ball.x, ball.y) == True:
                self.view.update_ball(ball.object_view, x1, y1, ball.x, ball.y)
                obstacle = self.model.grid[ball.y][ball.x]
                if obstacle != 0:
                    obstacle.affect_ball(ball)
            else:
                for i in range(len(self.model.balls)):
                    if self.model.balls[i] == ball:
                        self.view.window.supprimer(ball.object_view)
                        self.model.balls.pop(i)
                        print("------")
                        print(len(balls))
                        print(len(self.model.balls))
                        break
                print("break")
