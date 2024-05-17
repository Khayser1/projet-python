import pygame
from animaux import Animal

elephant1 = Animal(("elephant1.png"), (116,152), 25, 10)
elephant2 = Animal(("elephant2.png"), (116,76), 25, 170)
girafe1 = Animal(("girafe1.png"), (116,152), 25, 260)
girafe2 = Animal(("girafe2.png"), (58,152), 40, 425)
hipopo1 = Animal(("hipopotame1.png"), (174,76), 10, 590)
hipopo2 = Animal(("hipopotame2.png"), (116,76), 1105, 590)
lion1 = Animal(("lion1.png"), (116,152), 1105, 10)
lion2 = Animal(("lion2.png"), (116,76), 1105, 170)
zebre1 = Animal(("zebre1.png"), (58,152), 1120, 260)
zebre2 = Animal(("zebre2.png"), (116,76), 1105, 425)

 

def barre_droite(surface):
    bar_couleur=(125, 125, 113)
    bar_position=(1080,0,200,680)
    pygame.draw.rect(surface, bar_couleur, bar_position)
        
def barre_gauche(surface):
    bar_couleur = (125, 125, 113)   
    bar_position = (0, 0, 200, 680)     
    pygame.draw.rect(surface, bar_couleur, bar_position)
    
    


def level():
    if elephant1.rect1.center == (453,305):
        elephant1.valid = True
    elif elephant2.rect2.center == (513,305):
        elephant2.valid = True

    if elephant1.valid == elephant2.valid == True:
        return True


def retour():
    cpt = -1
    liste_animal = [elephant1.valid, elephant2.valid]
    for i in liste_animal:
        cpt += 1
        if i == False:
            return (liste_animal[cpt])
