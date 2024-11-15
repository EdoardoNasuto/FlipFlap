class Grid:
    """
    Représente une grille de jeu avec des obstacles et des billes.

    Attributes:
        width (int): La largeur de la grille.
        height (int): La hauteur de la grille.
        grid (list): La matrice représentant la grille.
        balls (list): La liste des billes ajoutées à la grille.
    """

    def __init__(self, width: int, height: int):
        """
        Initialise une grille de jeu avec la largeur et la hauteur.

        Args:
            width (int): La largeur de la grille.
            height (int): La hauteur de la grille.
        """
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
        self.balls = []

    def add_obstacle(self, x: int, y: int, obstacle: object) -> None:
        """
        Ajoute un obstacle à la grille à la position (x, y).

        Args:
            x (int): La position en x de l'obstacle.
            y (int): La position en y de l'obstacle.
            obstacle (object): L'obstacle à ajouter à la grille.
        """
        self.grid[x][y] = obstacle

    def add_ball(self, ball: object) -> None:
        """Ajoute une bille à la grille.

        Args:
            ball (object): La bille à ajouter à la grille.
        """
        self.balls.append(ball)

    def is_valid_position(self, x: int, y: int) -> bool:
        """Vérifie si la position (x, y) est valide (dans les limites de la grille).

        Args:
            x (int): La position en x.
            y (int): La position en y.

        Returns:
            bool: True si la position est valide, sinon False.
        """
        if 0 <= x < self.width and 0 <= x < self.width:
            return True
        return False

    def display(self) -> str:
        """ Affiche la grille avec les obstacles et billes pour le débogage. """
        for line in self.grid:
            print(line)
