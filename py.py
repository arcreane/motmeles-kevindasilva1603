
import random

# Liste des mots à mélanger
words = ['python', 'programmation', 'algorithme', 'machine', 'apprentissage', 'données']

# Création d'une grille de 10x5
grid = [[' ' for _ in range(10)] for _ in range(5)]

# Insérer des mots dans la grille
for word in words:
    # Choisir une direction aléatoire pour le mot (droite ou bas)
    direction = random.choice(['droite', 'bas'])
    # Choisir une position aléatoire pour le mot
    if direction == 'droite':
        row = random.randint(0, 4)
        col = random.randint(0, 10 - len(word))
    else:
        row = random.randint(0, 5 - len(word))
        col = random.randint(0, 9)
    # Insérer le mot dans la grille
    for i, letter in enumerate(word):
        if direction == 'droite':
            grid[row][col+i] = letter
        else:
            grid[row+i][col] = letter

# Remplir les cases restantes avec des lettres aléatoires
for row in range(5):
    for col in range(10):
        if grid[row][col] == ' ':
            grid[row][col] = chr(random.randint(65, 90))

# Afficher la grille
for row in grid:
    print(' '.join(row))
