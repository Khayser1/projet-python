import pygame
from lanceur import projectile
from lanceur_gauche import projectile_gauche
#classe du joueur 
class players(pygame.sprite.Sprite): #permet de definir la class comme sprite pour supeerpose un objet appart au dessus du fond 
    def __init__(self, jeux):
        super().__init__()
        self.jeux=jeux #j'appelle les caractéristique du jeux pour use dans check position
        self.health=100
        self.max_health=100
        self.attack=30
        self.velocity=1
        self.groupe_projectiles_droite=pygame.sprite.Group()#creer un groupe d'ensemble de projetile si on dn tire pls donc il seront ranger dans cette caracteristique  
        self.groupe_projectiles_gauche=pygame.sprite.Group()
        self.image=pygame.image.load('/Users/nicolascastagni/Desktop/dossier sans titre/PygameAssets-main/player.png')
        self.rect=self.image.get_rect() #la methode get_ret sert a generer un rectangle donc on met l'image du joueur sur le rectangle pour avoir la position
        self.rect.x=450 # permet de faire spwan l'image ou on veut quand ton lance 
        self.rect.y=500
    
    def dégats (self,nb_dégat_subit):
        if self.health-nb_dégat_subit>nb_dégat_subit:
             self.health-=nb_dégat_subit
        
    def barre_vie(self,surface):#surface ou va mettre la barre 
        #variable qui posséde les corrdonné de couleur 
        bar_couleur=(37, 143, 255)
        bar_couleur_fond=(1, 2, 3  )
        
        #variable qui posséde les dimension de la barre de vie 
        bar_position=[self.rect.x+50,self.rect.y+20,self.health,8]
        bar_position_fond=[self.rect.x+50,self.rect.y+20,self.max_health,8]
        #dessiner notre de fond de barre de vie 
        pygame.draw.rect(surface,bar_couleur_fond,bar_position_fond)
        #dessiner notre barre de vie pour cela ou creer un rectangle (rect) et on met ces caractéristique avec les variables ci dessus
        pygame.draw.rect(surface,bar_couleur,bar_position)
        
    
    def move_droite(self):
        # si le joueur n'est pas en colision avec les monstres
        if not self.jeux.check_collision(self, self.jeux.groupe_monstre):
            self.rect.x +=self.velocity
     
    def move_gauche(self):
        if not self.jeux.check_collision(self,self.jeux.groupe_monstre_gauche):
            self.rect.x -= self.velocity

    def move_haut(self):
        self.rect.y+=self.velocity
    def move_bas(self):
        self.rect.y-=self.velocity
        
    def lauch_projectile(self):
          #generer le projectile instance du projectile 
        self.groupe_projectiles_droite.add(projectile(self)) # on met tous les projectile dans le groupe
        
    def lauch_projectile_gauche(self):
        self.groupe_projectiles_gauche.add(projectile_gauche(self))
        
