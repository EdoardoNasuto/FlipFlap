from src.rules.params_rule import *
from src.rules.game_rules import *


def base_game(num_rows, num_columns, num_obstacles, num_balls, size, speed):
    """
    Configure le mode de jeu de base avec des obstacles et des billes placés aléatoirement.

    Args:
        num_rows (int): Le nombre de lignes dans la grille de jeu.
        num_columns (int): Le nombre de colonnes dans la grille de jeu.
        num_obstacles (int): Le nombre d'obstacles à placer dans la grille.
        num_balls (int): Le nombre de billes présentes dans le jeu.
        size (int): La taille de la grille de jeu.

    Notes:
        Le mode de jeu de base utilise des obstacles rouges, bleus et verts répartis
        selon les proportions spécifiées. Les billes sont placées de manière aléatoire,
        et les billes qui sortent de la grille sont supprimées.
    """
    GameRules(num_rows, num_columns, num_obstacles, num_balls, size, speed,
              obstacle_setup=ItemSetup.RANDOM, ball_setup=ItemSetup.RANDOM, item_type=ItemnType.BALLS,
              obstacle_color={"red": 0.34,
                              "blue": 0.33, "green": 0.33},
              ball_out_of_the_board=BallOutOfTheBoard.DELETE)


def trap_game(num_rows, num_columns, num_obstacles, num_balls, size, speed):
    """
    Configure le mode de jeu 'trap' avec des obstacles et des billes placés de manière spécifique.

    Args:
        num_rows (int): Le nombre de lignes dans la grille de jeu.
        num_columns (int): Le nombre de colonnes dans la grille de jeu.
        num_obstacles (int): Le nombre d'obstacles à placer dans la grille.
        num_balls (int): Le nombre de billes présentes dans le jeu.
        size (int): La taille de la grille de jeu.

    Notes:
        Les obstacles sont répartis uniformément dans la grille. Les billes sont placées de manière aléatoire.
        Les obstacles changent de couleur au fur et à mesure que des billes interagissent avec eux, et les billes
        traversent la grille au lieu d'être supprimées lorsqu'elles en sortent. Les joueurs peuvent également
        changer la couleur des obstacles ou ajouter des obstacles sur la grille.
    """
    GameRules(num_rows, num_columns, num_obstacles, num_balls, size, speed,
              obstacle_setup=ItemSetup.EQUALLY, ball_setup=ItemSetup.RANDOM, item_type=ItemnType.BALLS,
              obstacle_color={"red": 0.40, "blue": 0.30,
                              "green": 0.20, "white": 0.10},
              obstacle_in_game_color_change={"red": 0.40, "blue": 0.30,
                                             "green": 0.30},
              ball_out_of_the_board=BallOutOfTheBoard.TRAVERSE_BOARD,
              change_obstacle_color_if_ball_present=ChangeObstacleColor.RANDOM,
              change_obstacle_color_on_click=ChangeObstacleColor.RANDOM)


def poule_renard_vipere_game(num_rows, num_columns, num_obstacles, num_balls, size, speed):
    """
    Configure le mode de jeu 'Poule, Renard, Vipère' avec des animaux comme billes.

    Args:
        num_rows (int): Le nombre de lignes dans la grille de jeu.
        num_columns (int): Le nombre de colonnes dans la grille de jeu.
        num_obstacles (int): Le nombre d'obstacles à placer dans la grille.
        num_balls (int): Le nombre de billes présentes dans le jeu.
        size (int): La taille de la grille de jeu.

    Notes:
        Les billes sont représentées par des animaux et sont placées de manière équitable dans la grille.
        Les obstacles changent de couleur en fonction des interactions avec les billes. Les billes qui sortent
        de la grille traversent celle-ci au lieu d'être supprimées. Le jeu inclut des règles de collision entre
        les billes, simulant une chaîne alimentaire. Les joueurs peuvent choisir d'ajouter des obstacles ou
        de modifier les couleurs des obstacles.
    """
    GameRules(num_rows, num_columns, num_obstacles, num_balls, size, speed,

              obstacle_setup=ItemSetup.RANDOM, ball_setup=ItemSetup.EQUALLY, item_type=ItemnType.ANIMALS,

              obstacle_color={"red": 0.30, "blue": 0.30,
                              "green": 0.30, "purple": 0.10},
              obstacle_in_game_color_change={
                  "red": 0.34, "blue": 0.33, "green": 0.33},

              ball_out_of_the_board=BallOutOfTheBoard.TRAVERSE_BOARD,
              change_obstacle_color_if_ball_present=ChangeObstacleColor.RANDOM,
              ball_collision=BallCollision.SIMULATE_FOOD_CHAIN,

              players=3,
              players_choices=[[PlayerChoices.CHANGE_OBSTACLE_COLOR, ChangeObstacleColor.RANDOM],
                               [PlayerChoices.ADD_OBSTACLE, ChangeObstacleColor.RANDOM]],)
