from enum import Enum, auto


class ItemSetup (Enum):
    RANDOM = auto()
    EQUALLY = auto()


class ItemnType (Enum):
    BALLS = auto()
    ANIMALS = auto()


class BallOutOfTheBoard (Enum):
    DELETE = auto()
    TRAVERSE_BOARD = auto()


class ChangeObstacleColor (Enum):
    RANDOM = auto()
    WEIGHTED = auto()
    SEQUENTIAL = auto()


class BallCollision (Enum):
    SIMULATE_FOOD_CHAIN = auto()


class PlayerChoices (Enum):
    CHANGE_OBSTACLE_COLOR = "Changer la couleur d'un obstacle"
    ADD_OBSTACLE = "Ajouter un obstacle"
