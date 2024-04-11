import  pygame

class Animal(pygame.sprite.Sprite):
    def __init__ (self,piece):#piece = chemin de l'image selon l'animal
        super().__init__()        
        self.image=pygame.image.load(piece)
        self.image= pygame.transform.scale(self.image,(50,50))
        self.rect=self.image.get_rect()
        self.rect.x=200
        self.rect.y=300
    
    
    
    
    
    
    
    
    
        
        