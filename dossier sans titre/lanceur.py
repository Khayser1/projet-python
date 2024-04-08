import pygame 
class projectile(pygame.sprite.Sprite):
    
    def __init__(self,player ): #on met comme argument la classe player importer les corrdonner du joueur 
        super().__init__()
        self.velocity=1
        self.player=player# on appelle les caractéristique pour pouvoir les utilisé facilement dans les methodes
        self.image=pygame.image.load('/Users/nicolascastagni/Desktop/dossier sans titre/PygameAssets-main/projectile.png')
        self.image= pygame.transform.scale(self.image,(50,50)) # permet de modifier la taille du projectile 
        self.rect=self.image.get_rect()
        self.rect.x= player.rect.x+120 #on met comme position de spawn le joueur en x
        self.rect.y= player.rect.y+100 # on met comme position de spawn ce lui du joueur en y
        self.original_image=self.image
        self.angle=0
   
    def rotation(self):
        # faire tourner le projectile 
        self.angle+=1
        self.image=pygame.transform.rotozoom(self.original_image,self.angle,1)
        self.rect=self.image.get_rect(center=self.rect.center)
        
   
    def supprimé(self):
        self.player.groupe_projectiles_droite.remove(self)
        print("supprimé")
        

    def move_projectile(self):
        self.rect.x+= self.velocity 
        self.rotation()
        
        
        for monstres in self.player.jeux.check_collision(self, self.player.jeux.groupe_monstre): 
            monstres.dégats(self.player.attack)
            self.supprimé() 
        if self.rect.x>1080:
            self.supprimé()
            
            
    
        
        