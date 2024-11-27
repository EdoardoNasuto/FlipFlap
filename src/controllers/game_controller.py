from random import choice, choices

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
        self.view.refresh()
        self.start_game()

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
        import src.rules.game_mode_rules as mode
        if self.game_mode == "base":
            mode.base_game(self)
        elif self.game_mode == "trap":
            mode.trap_game(self)
        elif self.game_mode == "poule renard vipere":
            mode.poule_renard_vipere_game(self)
        self.view.exit_game()

    def move_ball(self, ball: Ball) -> bool:
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
            effect = obstacle.affect_ball(ball)
            if effect == "delete":
                self.remove_ball(ball)
            elif effect == "new_ball":
                print((self.model.ball_directions.index(
                    ball.direction) + 2) % 4)
                new_ball = self.model.add_ball(
                    ball.x, ball.y,
                    (self.model.ball_directions[((self.model.ball_directions.index(
                        ball.direction) + 2) % 4)]),
                    ball.animal)
                new_ball.object_view = self.view.draw_ball(
                    new_ball, f"assets/{ball.animal}.png")

    def change_obstacle_color_on_click(self, mode: str) -> None:
        """
        Gère les entrées de l'utilisateur, comme les clics sur la grille.
        """
        clic = self.view.recup_clic()
        if clic:
            obstacle = self.model.grid[clic.y //
                                       self.view.size][clic.x // self.view.size]
            if obstacle:
                self._change_obstacle_color(obstacle, mode)

    def change_obstacle_color_if_ball_present(self, ball: Ball, mode=str) -> None:
        """
        Gère l'interaction entre une bille et un obstacle.
        """
        obstacle = self.model.grid[ball.y][ball.x]
        if obstacle:
            # Si la bille est en contact avec un obstacle, change la couleur
            self._change_obstacle_color(obstacle, mode)

    def _change_obstacle_color(self, obstacle: Obstacle, mode: str = "sequential") -> None:
        """
        Change la couleur d'un obstacle.
        """

        valid_modes = {"random", "weighted", "sequential"}
        if mode not in valid_modes:
            raise ValueError(
                f"The mode must be one of the following values: {', '.join(valid_modes)}.")

        colors = list(self.model.obstacle_colors.keys())

        if obstacle.color in colors:
            if mode == "random":
                colors.remove(obstacle.color)
                obstacle.color = choice(colors)

            elif mode == "weighted":
                weights = list(self.model.obstacle_colors.values())
                weights.pop(colors.index(obstacle.color))
                colors.remove(obstacle.color)
                obstacle.color = choices(colors, weights=weights, k=1)[0]

            elif mode == "sequential":
                new_color = (colors.index(obstacle.color)+1) % len(colors)
                print(colors)
                print(obstacle.color)
                obstacle.color = colors[new_color]
                print(obstacle.color)

            self.view.update_obstacle_color(
                obstacle.object_view, obstacle.color)

    def remove_ball(self, ball: Ball):
        """
        Supprimer une bille du model et de la view
        """
        self.view.remove_ball(ball.object_view)
        self.model.remove_ball(ball)

    def ball_traverse_board(self, ball: Ball):
        """
        Fait traverser la grille à la bille
        """
        x1, y1 = ball.x, ball.y
        ball.traverse_board(self.model.num_columns-1, self.model.num_rows-1)
        self.view.update_ball_position(
            ball.object_view, x1, y1, ball.x, ball.y)
        self.update_ball_direction(ball)

    def simulate_food_chain(self):
        for ball in list(self.model.balls):
            for other_ball in list(self.model.balls):
                if other_ball is not ball:
                    if ball.x == other_ball.x:
                        if ball.y == other_ball.y:
                            if self.model.ball_animals.index(ball.animal) - 1 == self.model.ball_animals.index(other_ball.animal):
                                print(f"{other_ball.animal} --> {ball.animal}")
                                self.remove_ball(ball)
                    elif ball.x-1 == other_ball.x or ball.x+1 == other_ball.x:
                        if ball.y-1 == other_ball.y or ball.y+1 == other_ball.y:
                            if self.model.ball_directions[(self.model.ball_directions.index(ball.direction) + 2) % 4] == other_ball.direction:
                                print("ya")
                                print(f"{other_ball.animal} --> {ball.animal}")
                                self.remove_ball(ball)
