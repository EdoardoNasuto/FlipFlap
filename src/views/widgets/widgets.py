import tkinter as tk
from tkinter import ttk
from src.rules.params_rule import PlayerChoices


def integer_entry(parent, label, row, screen):
    tk.Label(parent, text=label).grid(
        row=row, column=0, padx=10, pady=5)

    validate_int = screen.register(_validate_integer)
    entry = tk.Entry(parent, validate="key",
                     validatecommand=(validate_int, "%P"))
    entry.grid(row=row, column=1, padx=10, pady=5)
    return entry


def enum_combobox(parent, label, enum_class, row, optional=False):
    tk.Label(parent, text=label).grid(row=row, column=0, padx=10, pady=5)
    choices = [item.name for item in enum_class]
    combobox = ttk.Combobox(parent, values=choices, state="readonly")
    combobox.grid(row=row, column=1, padx=10, pady=5)
    if optional:
        combobox.set("")
    return combobox


def multiple_color_and_weight_input(parent, label, row):
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


def player_choices(parent, row):
    tk.Label(parent, text="Choix des joueurs").grid(
        row=row, column=0, padx=10, pady=5)
    var1 = tk.IntVar()
    var2 = tk.IntVar()
    checkbox1 = tk.Checkbutton(
        parent, text=PlayerChoices.CHANGE_OBSTACLE_COLOR.value, variable=var1)
    checkbox2 = tk.Checkbutton(
        parent, text=PlayerChoices.ADD_OBSTACLE.value, variable=var2)
    checkbox1.grid(row=row, column=1, padx=10, pady=5)
    checkbox2.grid(row=row, column=2, padx=10, pady=5)
    return [var1, var2]


def _validate_integer(value):
    if value == "" or value.isdigit():
        return True
    else:
        return False
