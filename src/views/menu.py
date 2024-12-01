import tkinter as tk
from src.rules.params_rule import *
from src.rules.game_rules import *
from src.views.widgets.widgets import *
from src.rules.game_mode_rules import *


class Menu:
    """
    Cette classe utilise Tkinter pour créer une série d'écrans permettant aux utilisateurs 
    de personnaliser les paramètres du jeu, y compris la taille de la grille, le nombre d'obstacles, 
    le type d'éléments, et les règles avancées. Les paramètres configurés sont ensuite utilisés 
    pour lancer différentes variantes du jeu.
    """

    def __init__(self, root):
        """
        Initialise l'application et configure l'interface graphique principale.

        Args:
            root (tk.Tk): La fenêtre principale Tkinter.
        """
        self.screen = root
        self.screen.title("Interface de Configuration des Règles du Jeu")

        # Variables pour stocker les informations saisies
        self.game_rules = None

        # Création des frames pour chaque écran
        self.frame1 = self.create_frame1()
        self.frame2 = self.create_frame2()
        self.frame3 = self.create_frame3()
        self.frame4 = self.create_frame4()
        self.frame5 = self.create_frame5()

        # Afficher le premier écran
        self.frame1.pack()

    def create_frame1(self):
        """
        Crée la première interface utilisateur pour configurer les paramètres de base du jeu.

        Returns:
            tk.Frame: Frame contenant les widgets pour les paramètres de base.
        """
        frame = tk.Frame(self.screen)

        # ---------- PARAMETERS  ----------

        self.num_rows = integer_entry(
            frame, "Nombre de lignes", 0, self.screen)
        self.num_columns = integer_entry(
            frame, "Nombre de colonnes", 1, self.screen)
        self.num_obstacles = integer_entry(
            frame, "Nombre d'obstacles", 2, self.screen)
        self.num_balls = integer_entry(
            frame, "Nombre de boules", 3, self.screen)
        self.size = integer_entry(
            frame, "Taille de la grille", 4, self.screen)
        self.speed = integer_entry(
            frame, "Vitesse du jeu (1/10 s)", 5, self.screen)

        self.json_filename = tk.Entry(frame)
        self.json_filename.grid(row=6, column=1, padx=5, pady=5)
        label_import = tk.Label(
            frame, text="Nom du fichier JSON à importer")
        label_import.grid(row=6, column=0, padx=5, pady=5)

        self.export_filename = tk.Entry(frame)
        self.export_filename.grid(row=7, column=1, padx=5, pady=5)
        label_export = tk.Label(
            frame, text="Nom du fichier JSON à exporter")
        label_export.grid(row=7, column=0, padx=5, pady=5)

        # ---------- BUTTON  ----------

        next_button = tk.Button(frame, text="Configuration personalisé",
                                command=lambda: self.show_frame(self.frame2))
        next_button.grid(row=8, column=0, columnspan=2, pady=10)

        base_game_button = tk.Button(frame, text="Jeu de base",
                                     command=lambda: self.play_game_mode("base"))
        base_game_button.grid(row=9, column=0, columnspan=1, pady=5)

        trap_game_button = tk.Button(frame, text="Jeu de trap",
                                     command=lambda: self.play_game_mode("trap"))
        trap_game_button.grid(row=9, column=1, columnspan=1, pady=5)

        prv_game_button = tk.Button(frame, text="Poule Renard Vipere",
                                    command=lambda: self.play_game_mode("prv"))
        prv_game_button.grid(row=10, column=0, columnspan=2, pady=5)

        return frame

    def create_frame2(self):
        """
        Crée la deuxième interface utilisateur pour configurer les éléments du jeu.

        Returns:
            tk.Frame: Frame contenant les widgets pour configurer les éléments.
        """
        frame = tk.Frame(self.screen)

        # ---------- PARAMETERS  ----------

        self.item_type = enum_combobox(
            frame, "Type d'élément", ItemnType, 0)

        self.obstacle_setup = enum_combobox(
            frame, "Setup des obstacles", ItemSetup, 1)

        self.ball_setup = enum_combobox(
            frame, "Setup des boules", ItemSetup, 2)

        # ---------- BUTTON  ----------

        prev_button = tk.Button(frame, text="Précédent",
                                command=lambda: self.show_frame(self.frame1))
        prev_button.grid(row=3, column=0, pady=10)
        next_button = tk.Button(frame, text="Suivant",
                                command=lambda: self.show_frame(self.frame3))
        next_button.grid(row=3, column=1, pady=10)

        return frame

    def create_frame3(self):
        """
        Crée la troisième interface utilisateur pour configurer les couleurs et les poids des obstacles.

        Returns:
            tk.Frame: Frame contenant les widgets pour configurer les obstacles.
        """
        frame = tk.Frame(self.screen)

        # ---------- PARAMETERS  ----------

        self.obstacle_colors_and_weights = multiple_color_and_weight_input(
            frame, "Couleurs et poids des obstacles", 0)

        self.obstacle_in_game_color_change = multiple_color_and_weight_input(
            frame, "Couleurs et poids des obstacles in game", 1)

        # ---------- BUTTON  ----------

        prev_button = tk.Button(frame, text="Précédent",
                                command=lambda: self.show_frame(self.frame2))
        prev_button.grid(row=12, column=0, pady=10)
        next_button = tk.Button(frame, text="Suivant",
                                command=lambda: self.show_frame(self.frame4))
        next_button.grid(row=12, column=1, pady=10)

        return frame

    def create_frame4(self):
        """
        Crée la quatrième interface utilisateur pour configurer les règles avancées du jeu.

        Returns:
            tk.Frame: Frame contenant les widgets pour configurer les règles avancées.
        """
        frame = tk.Frame(self.screen)

        # ---------- PARAMETERS  ----------

        self.ball_out_of_the_board = enum_combobox(
            frame, "Ball Out of the Board", BallOutOfTheBoard, 0, optional=True)

        self.change_obstacle_color_on_click = enum_combobox(
            frame, "Change Obstacle Color on Click", ChangeObstacleColor, 2, optional=True)

        self.change_obstacle_color_if_ball_present = enum_combobox(
            frame, "Change Obstacle Color If Ball Present", ChangeObstacleColor, 3, optional=True)

        self.ball_collision = enum_combobox(
            frame, "Ball Collision", BallCollision, 4, optional=True)

        # ---------- BUTTON  ----------

        prev_button = tk.Button(frame, text="Précédent",
                                command=lambda: self.show_frame(self.frame3))
        prev_button.grid(row=5, column=0, pady=10)

        next_button = tk.Button(frame, text="Suivant",
                                command=lambda: self.show_frame(self.frame5))
        next_button.grid(row=5, column=1, pady=10)

        return frame

    def create_frame5(self):
        """
        Crée la cinquième interface utilisateur pour configurer les joueurs.

        Returns:
            tk.Frame: Frame contenant les widgets pour la configuration des joueurs.
        """
        frame = tk.Frame(self.screen)

        # ---------- PARAMETERS  ----------
        self.players = checkbutton(frame, "Mode Multijouer", 0)
        self.players_choices = []
        self.players_choices.append(checkbutton(
            frame, "Changer la couleur d'un obstacle", 1))
        self.players_choices.append(checkbutton(
            frame, "Ajouter un obstacle", 2))

        # ---------- BUTTON  ----------

        prev_button = tk.Button(frame, text="Précédent",
                                command=lambda: self.show_frame(self.frame3))
        prev_button.grid(row=3, column=0, columnspan=2, pady=10)

        validate_button = tk.Button(frame, text="Jouer",
                                    command=lambda: self.submit_game_rules())
        validate_button.grid(row=4, column=0, columnspan=2, pady=10)

        return frame

    def show_frame(self, frame_to_show):
        """
        Affiche un frame spécifique en masquant les autres frames.

        Args:
            frame_to_show (tk.Frame): Frame à afficher.
        """
        # Masquer tous les autres frames
        for frame in [self.frame1, self.frame2, self.frame3, self.frame4, self.frame5]:
            frame.pack_forget()

        # Afficher le frame demandé
        frame_to_show.pack()

    def play_game_mode(self, mode):
        """
        Lance le mode de jeu sélectionné avec les paramètres configurés.

        Args:
            mode (str): Le mode de jeu à lancer ("base", "trap", "prv").
        """
        # Récupérer et traiter les informations saisies
        json_filename = str(self.json_filename.get()
                            ) if self.json_filename != "" else None

        export_filename = str(self.export_filename.get()
                              ) if self.export_filename != "" else None

        num_rows = int(self.num_rows.get()) if not json_filename else None
        num_columns = int(self.num_columns.get())if not json_filename else None
        num_obstacles = int(self.num_obstacles.get()
                            )if not json_filename else None
        num_balls = int(self.num_balls.get())if not json_filename else None
        size = int(self.size.get())if not json_filename else None
        speed = float(self.speed.get())

        # Ferme la fenetre
        self.screen.destroy()

        if mode == "base":
            base_game(num_rows=num_rows, num_columns=num_columns,
                      num_obstacles=num_obstacles, num_balls=num_balls, size=size, speed=speed,
                      json_filename=json_filename, export_filename=export_filename)
        elif mode == "trap":
            trap_game(num_rows=num_rows, num_columns=num_columns,
                      num_obstacles=num_obstacles, num_balls=num_balls, size=size, speed=speed,
                      json_filename=json_filename, export_filename=export_filename)
        elif mode == "prv":
            poule_renard_vipere_game(num_rows=num_rows, num_columns=num_columns,
                                     num_obstacles=num_obstacles, num_balls=num_balls, size=size, speed=speed,
                                     json_filename=json_filename, export_filename=export_filename)

    def submit_game_rules(self):
        """
        Récupère les règles configurées et lance le jeu en utilisant ces règles.
        """
        # Récupérer et traiter les informations saisies
        json_filename = str(self.json_filename.get()
                            ) if self.json_filename != "" else None

        export_filename = str(self.export_filename.get()
                              ) if self.export_filename != "" else None

        num_rows = int(self.num_rows.get()) if not json_filename else None
        num_columns = int(self.num_columns.get())if not json_filename else None
        num_obstacles = int(self.num_obstacles.get()
                            )if not json_filename else None
        num_balls = int(self.num_balls.get())if not json_filename else None
        size = int(self.size.get())if not json_filename else None
        speed = float(self.speed.get())

        obstacle_setup = ItemSetup[self.obstacle_setup.get()]
        ball_setup = ItemSetup[self.ball_setup.get()]
        item_type = ItemnType[self.item_type.get()]

        # Récupérer les couleurs et poids
        obstacle_colors_and_weights = {
            color_combobox.get(): float(weight_entry.get()) / 100
            for color_combobox, weight_entry in self.obstacle_colors_and_weights
            if color_combobox.get() and weight_entry.get()
        }

        # Autres paramètres optionnels
        obstacle_in_game_color_change = {
            color_combobox.get(): float(weight_entry.get()) / 100
            for color_combobox, weight_entry in self.obstacle_colors_and_weights
            if color_combobox.get() and weight_entry.get()
        }
        ball_out_of_the_board = BallOutOfTheBoard[self.ball_out_of_the_board.get(
        )] if self.ball_out_of_the_board.get() else None
        change_obstacle_color_on_click = ChangeObstacleColor[self.change_obstacle_color_on_click.get(
        )] if self.change_obstacle_color_on_click.get() else None
        change_obstacle_color_if_ball_present = ChangeObstacleColor[self.change_obstacle_color_if_ball_present.get(
        )] if self.change_obstacle_color_if_ball_present.get() else None
        ball_collision = BallCollision[self.ball_collision.get(
        )] if self.ball_collision.get() else None

        players = 3 if bool(self.players.get()) else None
        player_choices = None

        if players != None:
            player_choices = []
            print(self.change_obstacle_color_on_click)
            if self.players_choices[0].get():
                player_choices.append(
                    [PlayerChoices.CHANGE_OBSTACLE_COLOR, change_obstacle_color_on_click])
            if self.players_choices[1].get():
                player_choices.append(
                    [PlayerChoices.ADD_OBSTACLE, change_obstacle_color_on_click])
            print(player_choices)

        self.screen.destroy()

        self.game_rules = GameRules(
            num_rows=num_rows, num_columns=num_columns, num_obstacles=num_obstacles, num_balls=num_balls, size=size, speed=speed,
            json_filename=json_filename, export_filename=export_filename,
            obstacle_setup=obstacle_setup, ball_setup=ball_setup, item_type=item_type,
            obstacle_color=obstacle_colors_and_weights,
            obstacle_in_game_color_change=obstacle_in_game_color_change,
            ball_out_of_the_board=ball_out_of_the_board,
            change_obstacle_color_on_click=change_obstacle_color_on_click,
            change_obstacle_color_if_ball_present=change_obstacle_color_if_ball_present,
            ball_collision=ball_collision,
            players=players,
            players_choices=player_choices
        )
