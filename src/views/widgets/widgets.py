import tkinter as tk
from tkinter import ttk
from src.rules.params_rule import PlayerChoices


def integer_entry(parent: tk.Widget, label: str, row: int, screen: tk.Tk) -> tk.Entry:
    """
    Crée un champ de saisie pour un entier, avec une validation des entrées.

    Args:
        parent (tk.Widget): Le widget parent dans lequel le champ de saisie sera placé.
        label (str): Le texte du label à afficher pour ce champ.
        row (int): La ligne de la grille où le widget sera positionné.
        screen (tk.Tk): La fenêtre principale de l'application, utilisée pour enregistrer la validation.

    Returns:
        tk.Entry: Le champ de saisie créé.
    """
    tk.Label(parent, text=label).grid(
        row=row, column=0, padx=10, pady=5)

    validate_int = screen.register(_validate_integer)
    entry = tk.Entry(parent, validate="key",
                     validatecommand=(validate_int, "%P"))
    entry.grid(row=row, column=1, padx=10, pady=5)
    return entry


def enum_combobox(parent: tk.Widget, label: str, enum_class, row: int, optional: bool = False) -> ttk.Combobox:
    """
    Crée un menu déroulant (Combobox) pour sélectionner une valeur d'une enum.

    Args:
        parent (tk.Widget): Le widget parent dans lequel la combobox sera placée.
        label (str): Le texte du label à afficher pour ce menu déroulant.
        enum_class (Enum): La classe d'énumération contenant les valeurs à afficher.
        row (int): La ligne de la grille où le widget sera positionné.
        optional (bool): Si vrai, le combobox sera initialisé avec une valeur vide.

    Returns:
        ttk.Combobox: Le menu déroulant créé.
    """
    tk.Label(parent, text=label).grid(row=row, column=0, padx=10, pady=5)
    choices = [item.name for item in enum_class]
    combobox = ttk.Combobox(parent, values=choices, state="readonly")
    combobox.grid(row=row, column=1, padx=10, pady=5)
    if optional:
        combobox.set("")
    return combobox


def multiple_color_and_weight_input(parent: tk.Widget, label: str, row: int) -> None:
    """
    Crée plusieurs champs de saisie pour associer des couleurs avec des poids.

    Args:
        parent (tk.Widget): Le widget parent dans lequel les champs seront placés.
        label (str): Le texte du label à afficher pour cette section.
        row (int): La ligne de la grille où les widgets seront positionnés.

    Returns:
        list: Une liste de tuples contenant les comboboxes de couleur et les champs de poids.
    """
    colors = ["red", "blue", "green", "white", "purple"]
    row = row * len(colors)
    tk.Label(parent, text=label).grid(
        row=row, column=0, padx=10, pady=5)
    color_comboboxes = []
    weight_entries = []

    for i in range(len(colors)):
        color_combobox = ttk.Combobox(
            parent, values=colors, state="readonly")
        color_combobox.grid(row=row + i, column=1, padx=10, pady=5)
        color_comboboxes.append(color_combobox)

        tk.Label(parent, text="Poids (%)").grid(
            row=row + i, column=2, padx=10, pady=5)
        weight_entry = tk.Entry(parent)
        weight_entry.grid(row=row + i, column=3, padx=10, pady=5)
        weight_entries.append(weight_entry)

    return list(zip(color_comboboxes, weight_entries))


def checkbutton(parent: tk.Widget, text: str, row: int) -> bool:
    """
    Crée un Checkbutton.

    Args:
        parent (tk.Widget): Le widget parent dans lequel le Checkbutton sera placé.
        label (str): Le texte du label à afficher pour cette option.
        row (int): La ligne de la grille où le widget sera positionné.

    Returns:
        bool: True si le Checkbutton est coché, sinon False.
    """
    # Créer la variable associée au Checkbutton
    var = tk.IntVar()

    # Créer le Checkbutton et le placer dans la grille
    checkbutton = tk.Checkbutton(
        parent, text=text, variable=var
    )
    checkbutton.grid(row=row, column=1, padx=10, pady=5)

    return var


def _validate_integer(value: str) -> bool:
    """
    Fonction de validation pour s'assurer que la valeur saisie est un entier.

    Args:
        value (str): La valeur à valider.

    Returns:
        bool: Retourne True si la valeur est valide, sinon False.
    """
    if value == "" or value.isdigit():
        return True
    else:
        return False
