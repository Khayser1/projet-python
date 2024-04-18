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




elephant1=Animal('/Users/nicolascastagni/Desktop/Jeu /Assets /elephant1.png',880,10)
elephant2=Animal('/Users/nicolascastagni/Desktop/Jeu /Assets /elephant2.png',880,200)
girafe1=Animal('/Users/nicolascastagni/Desktop/Jeu /Assets /girafe1.png',880,390)
girafe2=Animal('/Users/nicolascastagni/Desktop/Jeu /Assets /girafe2.png',880,580)
hipopo1=Animal('/Users/nicolascastagni/Desktop/Jeu /Assets /hippopotame1.png',150,10)
hipopo2=Animal('/Users/nicolascastagni/Desktop/Jeu /Assets /hippopotame2.png',150,200)
lion1=Animal('/Users/nicolascastagni/Desktop/Jeu /Assets /lion1.png',150,390)
lion2=Animal('/Users/nicolascastagni/Desktop/Jeu /Assets /lion2.png',150,580)
zebre1=Animal('/Users/nicolascastagni/Desktop/Jeu /Assets /zebre1.png',150,770)
zebre2=Animal('/Users/nicolascastagni/Desktop/Jeu /Assets /zebre2.png',880,770)

ouvert = True #cette permet de definir pour le programme si la fenetre est en court d'éxecution
moving = False 

#boucle tant que ouvert est vrai pour que le fenètre reste ouvert 
while ouvert:
    
    #appliquer l'arriere plan de notre jeu car pygame.display.set_mode((500,300))genere une surface et pygame.image.load('assets/fond.jpg.avif') notre fond suffit de mettre le fond sur la surface
    surface.blit(Fond_image, (0,0))#blit permet de mettre notre image sur la   surface 
    
    
    barre_droite(surface)
    barre_gauche(surface)
    
    #appliquer la carte éléphant 
    surface.blit(elephant1.image,elephant1.rect)
    surface.blit(elephant2.image,elephant2.rect)
    surface.blit(girafe1.image,girafe1.rect)
    surface.blit(girafe2.image,girafe2.rect)
    surface.blit(hipopo1.image,hipopo1.rect)
    surface.blit(hipopo2.image,hipopo2.rect)
    surface.blit(lion1.image,lion1.rect)
    surface.blit(lion2.image,lion2.rect)
    surface.blit(zebre1.image,zebre1.rect)
    surface.blit(zebre2.image,zebre2.rect)
    
    
    #mettre jour notre ecrans écrans car la c'est fixe
    pygame.display.flip()#flip permet de mettre a jour l'ecrans 
    
    
    
    #si le joueur ferme cette fenetre 
    for event in pygame.event.get():#get est une liste d'évenement 
        #l'evenement fermeture de fenetre
        if event.type==pygame.QUIT:
            ouvert=False  # si le joueur quitte la varriable devient false 
            pygame.quit()
        elif event.type==pygame.MOUSEBUTTONDOWN:
            if lion1.rect.collidepoint(event.pos):
                moving = True  
        elif event.type == pygame.MOUSEBUTTONUP:          
           moving = False
        elif event.type == pygame.MOUSEMOTION and moving:
            lion1.rect.move_ip(event.rel)
            
            
            
        