import pygame
from animaux import Animal

elephant1 = Animal(("/Users/nicolascastagni/Desktop/main fouc /images /elephant1.png"), (116,152), 25, 10)
elephant2 = Animal(("/Users/nicolascastagni/Desktop/main fouc /images /elephant2.png"), (116,76), 25, 170)
girafe1 = Animal(("/Users/nicolascastagni/Desktop/main fouc /images /girafe1.png"), (116,152), 25, 260)
girafe2 = Animal(("/Users/nicolascastagni/Desktop/main fouc /images /girafe2.png"), (58,152), 40, 425)
hipopo1 = Animal(("/Users/nicolascastagni/Desktop/main fouc /images /hipopotame1.png"), (174,76), 10, 590)
hipopo2 = Animal(("/Users/nicolascastagni/Desktop/main fouc /images /hipopotame2.png"), (116,76), 1105, 590)
lion1 = Animal(("/Users/nicolascastagni/Desktop/main fouc /images /lion1.png"), (116,152), 1105, 10)
lion2 = Animal(("/Users/nicolascastagni/Desktop/main fouc /images /lion2.png"), (116,76), 1105, 170)
zebre1 = Animal(("/Users/nicolascastagni/Desktop/main fouc /images /zebre1.png"), (58,152), 1120, 260)
zebre2 = Animal(("/Users/nicolascastagni/Desktop/main fouc /images /zebre2.png"), (116,76), 1105, 425)

 

def barre_droite(surface):
    bar_couleur=(125, 125, 113)
    bar_position=(1080,0,200,680)
    pygame.draw.rect(surface, bar_couleur, bar_position)
        
def barre_gauche(surface):
    bar_couleur = (125, 125, 113)   
    bar_position = (0, 0, 200, 680)     
    pygame.draw.rect(surface, bar_couleur, bar_position)
    
    
valid_animal = [elephant1.valid, elephant2.valid]