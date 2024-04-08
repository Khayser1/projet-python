import pygame
import random

class monstre_gauche(pygame.sprite.Sprite): 
    def __init__(self,jeux):
        super().__init__()
        self.jeux=jeux
        self.health=15
        self.max_health=100
        self.attack=0.3
        self.velocity=random.randint(1,3)
        self.image=pygame.image.load('/Users/nicolascastagni/Desktop/dossier sans titre/PygameAssets-main/mummy/mummy1.png')
        self.rect=self.image.get_rect()
        self.rect.x=-80-random.randint(0,300)
        self.rect.y=540
        
    def barre_vie_monstre_gauche(self,surface):#surface ou va mettre la barre 
        #variable qui posséde les corrdonné de couleur 
        bar_couleur=(37, 143, 255)
        bar_couleur_fond=(1, 2, 3  )
        bar_position_fond=[self.rect.x+10,self.rect.y-20,self.max_health,8]
        #variable qui posséde les dimension de la barre de vie 
        bar_position=[self.rect.x+10,self.rect.y-20,self.health,8]
        pygame.draw.rect(surface,bar_couleur_fond,bar_position_fond)
        #dessiner notre barre de vie pour cela ou creer un rectangle (rect) et on met ces caractéristique avec les variables ci dessus
        pygame.draw.rect(surface,bar_couleur,bar_position)
        
   
    def dégats_gauche(self,nb_dégat_subit):
        self.health-=nb_dégat_subit
        
        if self.health<=0:
            self.rect.x=-80-random.randint(0,300)
            self.health=self.max_health

        
        
    def move_monstre_gauche(self):
        if not self.jeux.check_collision(self, self.jeux.groupe_player):
         self.rect.x+=self.velocity
        else:
            self.jeux.player.dégats(self.attack)