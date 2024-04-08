import pygame 
from Joueur import players
from monstre import monstre
from monstre_gauche import monstre_gauche

#classe jeu 
class jeu:
    def __init__(self):
        self.groupe_player=pygame.sprite.Group()# creer un groupe que pour le joueur pour comparé groupe a groupe pour les colisions et que je joueur reste bloquer
        self.player=players(self)# generer le joueur 
        self.groupe_player.add(self.player)#on met notre joueur directement dans son groupe vu qu'il est tous seul et pas besoins d'actionner un  truc pour le mettre dedans pas comme les projectiles et monstres
        self.toucheAppuyer={}
        self.groupe_monstre=pygame.sprite.Group()
        self.groupe_monstre_gauche=pygame.sprite.Group()
        self.spawn_monstres()# en generer 2
        self.spawn_monstres()#pour generer automatiquement les monstres automatiquement vue que cette classe est generer direct au demarrage 
        self.spawn_monstres_gauche()
        self.spawn_monstres_gauche()
           
        
    def spawn_monstres(self):
        monstres= monstre(self)
        self.groupe_monstre.add(monstres)# ajouter les monstres dans le groupe comme les projectiles 
        
    def spawn_monstres_gauche(self):
        monstres=monstre_gauche(self)
        self.groupe_monstre_gauche.add(monstres)
    
    
    #verifier les colisions entre les entités donc en verifiant leur positions
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)