from time import sleep

from src.views.game_view import GameView
from src.models.grid_model import Grid


class GameController:
    """
    Gère la logique de contrôle pour la simulation, incluant la grille, les obstacles, les billes et l'interface graphique.

    Attributes:
        model (Grid): La grille contenant les obstacles et les billes.
        view (GameView): L'interface graphique pour afficher la simulation.
        speed (float): La vitesse de la simulation, par défaut 0.1.
    """

    def __init__(self, grid: Grid, gui: GameView, speed: float = 0.1):
        """
        Initialise le contrôleur avec une grille, une vue, et configure les obstacles et billes.

        Args:
            grid (Grid): L'instance de la grille utilisée pour la simulation.
            gui (GameView): L'interface graphique pour la simulation.
            speed (float, optionnel): La vitesse de la simulation, par défaut 0.1.
        """
        self.model = grid
        self.view = gui
        self.speed = speed
        self.setup_obstacles()
        self.setup_grid()
        self.setup_balls()
        self.start_game()

    def setup_grid(self) -> None:
        """
        Dessine les cases de la grille.
        """
        self.view.draw_grid(self.model.num_rows, self.model.num_columns)

    def setup_obstacles(self):
        """ Dessine tout les obstacles de la grille """
        for column in range(self.model.num_columns):
            for row in range(self.model.num_rows):
                obstacle = self.model.grid[row][column]
                if obstacle:
                    self.view.draw_obstacle(
                        obstacle.x, obstacle.y, obstacle.color)

    def setup_balls(self) -> None:
        """ Dessine toutes les billes sur la grille. """
        for ball in self.model.balls:
            ball.object_view = self.view.draw_ball(ball)

    def start_game(self):
        """ Démarre la simulation en exécutant des rounds jusqu'à ce qu'il n'y ait plus de billes dans la grille. """
        while len(self.model.balls) > 0:
            sleep(self.speed)
            self.run_round()
            self.view.refresh()
        self.view.exit_game()

    def run_round(self):
        """ Lance un round de simulation dans laquelle les billes interagissent avec les obstacles et se déplacent sur la grille. """
        balls = list(self.model.balls)  # Prendre la liste et pas la variable
        for ball in balls:
            x1, y1 = ball.x, ball.y
            ball.move()
            if self.model.is_valid_position(ball.x, ball.y):
                self.view.update_ball(ball.object_view, x1, y1, ball.x, ball.y)
                obstacle = self.model.grid[ball.y][ball.x]
                obstacle.affect_ball(ball) if obstacle else ...
            else:
                self.view.remove_ball(ball.object_view)
                self.model.remove_ball(ball)
