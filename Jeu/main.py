import pygame
from Jeux import*
from animaux import Animal
pygame.init() # charger les composants dans le module pygame

#generer la fenetre 
pygame.display.set_caption("Arche de noé")#display et en rapport avec la fenetre et set_caption permet generer et de donner un titre a la fenetre et rajouter un logo")
surface = pygame.display.set_mode((1080,720))#set_permet de dimensionner le fenetre  en generant une surface 

#importer l'arriere plan du jeu  
Fond_image= pygame.image.load('/Users/nicolascastagni/Desktop/Jeu /Assets /fond mer .jpg')
#charger l'image de depuis un chemin de l'ordi  




elephant1=Animal('/Users/nicolascastagni/Desktop/Jeu /Assets /image animaux /elephant1.jpg')

ouvert = True #cette permet de definir pour le programme si la fenetre est en court d'éxecution

#boucle tant que ouvert est vrai pour que le fenètre reste ouvert 
while ouvert:
    
    #appliquer l'arriere plan de notre jeu car pygame.display.set_mode((500,300))genere une surface et pygame.image.load('assets/fond.jpg.avif') notre fond suffit de mettre le fond sur la surface
    surface.blit(Fond_image, (0,0))#blit permet de mettre notre image sur la   surface 
    
    #appliquer la carte éléphant 
    surface.blit(elephant1.image,elephant1.rect)
    barre_droite(surface)
    
    
    #mettre jour notre ecrans écrans car la c'est fixe
    pygame.display.flip()#flip permet de mettre a jour l'ecrans 
    
    
    
    #si le joueur ferme cette fenetre 
    for event in pygame.event.get():#get est une liste d'évenement 
        #l'evenement fermeture de fenetre
        if event.type==pygame.QUIT:
            ouvert=False  # si le joueur quitte la varriable devient false 
            pygame.quit()
            
            
            