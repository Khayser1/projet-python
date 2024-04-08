import pygame
from Jeux import jeu
pygame.init() # charger les composants dans le module pygame

        
    
#generer la fenetre 
pygame.display.set_caption("Arche de noé")#display et en rapport avec la fenetre et set_caption permet generer et de donner un titre a la fenetre et rajouter un logo")
surface = pygame.display.set_mode((1080,720))#set_permet de dimensionner le fenetre  en generant une surface 

#importer l'arriere plan du jeu  
Fond_image= pygame.image.load('/Users/nicolascastagni/Desktop/dossier sans titre/PygameAssets-main/bg.jpg')
#charger l'image de depuis un chemin de l'ordi  


#generer jeux 
jeux =jeu()




ouvert = True #cette permet de definir pour le programme si la fenetre est en court d'éxecution

#boucle tant que ouvert est vrai pour que le fenètre reste ouvert 
while ouvert:
    
    #appliquer l'arriere plan de notre jeu car pygame.display.set_mode((500,300))genere une surface et pygame.image.load('assets/fond.jpg.avif') notre fond suffit de mettre le fond sur la surface
    surface.blit(Fond_image, (0,-200))#blit permet de mettre notre image sur la   surface 
    
    #mettre le joueur sur la fenetre 
    surface.blit(jeux.player.image,jeux.player.rect) 
    jeux.player.barre_vie(surface)
    
    
    # recuperer l'ensemble des projectile dans le groupe et leurs donner la vitesse
    for projectile in jeux.player.groupe_projectiles_droite:
        projectile.move_projectile()
        
    for projectile_gauche in jeux.player.groupe_projectiles_gauche:
        projectile_gauche.move_projectile_gauche()
    
    #recupere l'ensembles de monstre et bouger
    for monstres in jeux.groupe_monstre:
        monstres.move_monstre_droite()
        monstres.barre_vie(surface)#on met la barre de vie sur le monstre 
    
    for monstres in jeux.groupe_monstre_gauche:
        monstres.move_monstre_gauche()
        monstres.barre_vie_monstre_gauche(surface)
        
    #mettre les projectile sur la fenetre 
    jeux.player.groupe_projectiles_droite.draw(surface)
    jeux.player.groupe_projectiles_gauche.draw(surface)
    
    #mettre les monstres sur la fenetre
    jeux.groupe_monstre.draw(surface)
    jeux.groupe_monstre_gauche.draw(surface)
    
    
    if jeux.toucheAppuyer.get(pygame.K_RIGHT) and jeux.player.rect.x<=914:
        jeux.player.move_droite()
    elif jeux.toucheAppuyer.get(pygame.K_LEFT) and jeux.player.rect.x >=-35:
         jeux.player.move_gauche()
    print(jeux.player.rect.x)
    
     
    
    #mettre jour notre ecrans écrans car la c'est fixe
    pygame.display.flip()#flip permet de mettre a jour l'ecrans 
    
    
    #si le joueur ferme cette fenetre 
    for event in pygame.event.get():#get est une liste d'évenement 
        #l'evenement fermeture de fenetre
        if event.type==pygame.QUIT:
            ouvert=False  # si le joueur quitte la varriable devient false 
            pygame.quit()
        elif  event.type==pygame.KEYDOWN: #evenement du type touche appuyer (keydown)
            jeux.toucheAppuyer[event.key]=True 
            if event.key==pygame.K_e:
                jeux.player.lauch_projectile()
            if event.key==pygame.K_a:
                jeux.player.lauch_projectile_gauche()
            
        elif event.type==pygame.KEYUP:
            jeux.toucheAppuyer[event.key]=False
        
           
             
            
            
