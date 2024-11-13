# FlipFlap

## Prérequis

- [Git](https://git-scm.com/downloads) doit être installé sur votre machine.
- [Python 3.9+](https://www.python.org/downloads/) doit être installé.

## Installation

Suivez les étapes ci-dessous pour installer et exécuter ce projet en local.

### 1. Cloner le dépôt

Clonez ce projet en utilisant la commande suivante :

```bash
git clone https://github.com/EdoardoNasuto/FlipFlap
```

### 2. Créer un environnement virtuel

Créez un environnement virtuel Python pour isoler les dépendances du projet :

```bash
python -m venv .venv
```

Ici, `.venv` est le nom de l'environnement virtuel, mais vous pouvez choisir n'importe quel nom.

### 3. Activer l'environnement virtuel

Pour activer l'environnement virtuel, utilisez la commande appropriée en fonction de votre système d'exploitation :

- **Sur Windows** :

  ```bash
  .\.venv\Scripts\activate
  ```

- **Sur macOS et Linux** :

  ```bash
  source .venv/bin/activate
  ```

### 4. Installer les dépendances

Une fois l'environnement virtuel activé, installez les dépendances du projet avec :

```bash
pip install -r requirements.txt
```

Cette commande va installer toutes les bibliothèques listées dans le fichier `requirements.txt`.

### 5. Exécuter le projet

Pour lancer le projet, utilisez la commande suivante (adaptez selon votre projet) :

```bash
python main.py
```

## Désactiver l'environnement virtuel

Après avoir terminé, vous pouvez désactiver l'environnement virtuel en tapant :

```bash
deactivate
```