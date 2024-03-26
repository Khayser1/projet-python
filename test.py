import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((800, 600))
# Taille de la grille
largeur = 5
hauteur = 5

# Créer une surface pour la grille
grille_surface = pygame.Surface((largeur * CASE_SIZE, hauteur * CASE_SIZE))

# Créer une liste pour stocker les cases
grille = [[0 for i in range(largeur)] for j in range(hauteur)]
