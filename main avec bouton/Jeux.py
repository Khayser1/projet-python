import pygame
from animaux import Animal 




   
   
   
     
    
        
        
def barre_droite(surface):
    bar_couleur=(125, 125, 113)
    bar_position=(1080,0,200,680)
    pygame.draw.rect(surface,bar_couleur,bar_position)
        
def barre_gauche(surface):
    bar_couleur=(125, 125, 113)
    bar_position=(0, 0, 200, 680)
    pygame.draw.rect(surface,bar_couleur,bar_position)
    
