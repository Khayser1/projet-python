import pygame

pygame.init()
taille_fenetre = (500,400)
screen_surface = pygame.display.set_mode(taille_fenetre)

continuer = True
while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False


pygame.quit()