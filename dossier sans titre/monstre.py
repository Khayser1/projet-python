import pygame 
import random #pour generer aleatoirement la vitesse des monstres et la position

class monstre(pygame.sprite.Sprite): 
    def __init__(self,jeux):
        super().__init__()
        self.jeux=jeux
        self.health=50
        self.max_health=100
        self.attack=0.3
        self.velocity=random.randint(1,3)
        self.image=pygame.image.load('/Users/nicolascastagni/Desktop/dossier sans titre/PygameAssets-main/mummy/mummy1.png')
        self.rect=self.image.get_rect()
        self.rect.x=1080+random.randint(0,300) # je rajoute au hasard une valeur entre 0 et 300 comme distance pour spawn
        self.rect.y=540
    
    
        
    def dégats (self,nb_dégat_subit):
        self.health-=nb_dégat_subit
        
        if self.health<=0:
            self.rect.x=1080+random.randint(0,300)
            self.velocity=random.randint(1,3) 
            self.health=self.max_health
        
    def barre_vie(self,surface):#surface ou va mettre la barre 
        #variable qui posséde les corrdonné de couleur 
        bar_couleur=(37, 143, 255)
        bar_couleur_fond=(1, 2, 3  )
        
        #variable qui posséde les dimension de la barre de vie 
        bar_position=[self.rect.x+10,self.rect.y-20,self.health,8]
        bar_position_fond=[self.rect.x+10,self.rect.y-20,self.max_health,8]
        #dessiner notre de fond de barre de vie 
        pygame.draw.rect(surface,bar_couleur_fond,bar_position_fond)
        #dessiner notre barre de vie pour cela ou creer un rectangle (rect) et on met ces caractéristique avec les variables ci dessus
        pygame.draw.rect(surface,bar_couleur,bar_position)
        
        
        
    def move_monstre_droite(self):
        if not self.jeux.check_collision(self, self.jeux.groupe_player):
            self.rect.x-=self.velocity
        else:
            self.jeux.player.dégats(self.attack)
        