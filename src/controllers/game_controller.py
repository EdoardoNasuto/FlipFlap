from random import choice

from src.views.game_view import GameView
from src.models.grid_model import Grid
from src.models.ball_model import Ball
from src.models.obstacle_model import Obstacle


class GameController:
    """
    Gère la logique de contrôle pour la simulation, incluant la grille, les obstacles, les billes et l'interface graphique.

    Attributes:
        model (Grid): La grille contenant les obstacles et les billes.
        view (GameView): L'interface graphique pour afficher la simulation.
        speed (float): La vitesse de la simulation, par défaut 0.1.
    """

    def __init__(self, grid: Grid, gui: GameView, speed: float = 0.1, game_mode: str = "base"):
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
        self.game_mode = game_mode
        self.setup_obstacles()
        self.setup_grid()
        self.setup_balls()
        self.view.refresh()
        self.start_game()

    # -- Setup Methods --

    def setup_obstacles(self):
        """
        Dessine tout les obstacles de la grille
        """
        for column in range(self.model.num_columns):
            for row in range(self.model.num_rows):
                obstacle = self.model.grid[row][column]
                if obstacle:
                    obstacle.object_view = self.view.draw_obstacle(
                        obstacle.x, obstacle.y, obstacle.color)

    def setup_grid(self) -> None:
        """
        Dessine les cases de la grille.
        """
        self.view.draw_grid(self.model.num_rows, self.model.num_columns)

    def setup_balls(self) -> None:
        """
        Dessine toutes les billes sur la grille.
        """
        for ball in self.model.balls:
            ball.object_view = self.view.draw_ball(ball)

    # -- Game Logic Methods --

    def start_game(self) -> None:
        """
        Démarre le jeu en fonction du mode choisi.
        """
        self.run_simulation()

    def run_simulation(self) -> None:
        """
        Exécute les rounds du jeu, adapté au mode.
        """
        self.view.refresh()
        import src.controllers.game_mode_controller as mode
        if self.game_mode == "base":
            mode.base_game(self)
        elif self.game_mode == "trap":
            mode.trap_game(self)
        self.view.exit_game()

    def update_ball_position(self, ball: Ball) -> bool:
        """
        Met à jour la position d'une bille et interagit avec les obstacles.
        """
        x1, y1 = ball.x, ball.y
        dx, dy = ball.move(test=True)
        if self.model.is_valid_position(x1 + dx, y1 + dy):
            ball.move()
            self.view.update_ball_position(
                ball.object_view, x1, y1, ball.x, ball.y)
            self.update_ball_direction(ball)
            return True
        return False

    def update_ball_direction(self, ball: Ball) -> None:
        """
        Gère l'interaction entre une bille et un obstacle.
        """
        obstacle = self.model.grid[ball.y][ball.x]
        if obstacle:
            obstacle.affect_ball(ball)

    def handle_user_input(self) -> None:
        """
        Gère les entrées de l'utilisateur, comme les clics sur la grille.
        """
        clic = self.view.recup_clic()
        if clic:
            obstacle = self.model.grid[clic.y //
                                       self.view.size][clic.x // self.view.size]
            if obstacle:
                self.change_obstacle_color(obstacle)

    def interact_with_obstacle(self, ball: Ball) -> None:
        """
        Gère l'interaction entre une bille et un obstacle.
        """
        obstacle = self.model.grid[ball.y][ball.x]
        if obstacle:
            # Si la bille est en contact avec un obstacle, change la couleur
            self.change_obstacle_color(obstacle)

    def change_obstacle_color(self, obstacle: Obstacle) -> None:
        """
        Change la couleur d'un obstacle.
        """
        colors = list(self.model.obstacle_colors)
        colors.remove(obstacle.color)
        obstacle.color = choice(colors)
        print("test")
        self.view.update_obstacle_color(obstacle.object_view, obstacle.color)

    def remove_ball(self, ball: Ball):
        """
        Supprimer une bille du model et de la view
        """
        self.view.remove_ball(ball.object_view)
        self.model.remove_ball(ball)
