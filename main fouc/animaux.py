import pygame
pygame.init()

class Animal(pygame.sprite.Sprite):
    def __init__ (self, piece, taille, pos_x, pos_y):#piece = chemin de l'image selon l'animal
        super().__init__()
        self.image = pygame.image.load(piece)
        self.taille = taille
        self.image = pygame.transform.scale(self.image, self.taille)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.pos = pygame.mouse.get_pos()
        self.rel = pygame.mouse.get_rel()
        self.rect1 = self.image.get_rect()            
        self.rect2 = self.image.get_rect()
        self.rect3 = self.image.get_rect()
        self.rect4 = self.image.get_rect()
        self.rect5 = self.image.get_rect()
        self.creation_rect()
        self.valid = False
            

    def creation_rect(self):
        if self.taille == (116,152):
            self.rect1.bottomright = (self.rect.centerx+60, self.rect.centery+80)
            self.rect1.size = (58,76)
            self.rect2.topright = (self.rect.centerx+60, self.rect.centery)
            self.rect2.size = (58,76)
            self.rect3.bottomleft = (self.rect.centerx, self.rect.centery)
            self.rect3.size = (58,76)
            self.rect4.topleft = (self.rect.centerx, self.rect.centery)
            self.rect4.size = (58,76)
            self.rect5 = None

        elif self.taille == (116,76):
            self.rect1 = None
            self.rect2.midright = (self.rect.centerx+60, self.rect.centery) 
            self.rect2.size = (58,76)
            self.rect3 = None
            self.rect4.midleft = (self.rect.centerx, self.rect.centery) 
            self.rect4.size = (58,76)
            self.rect5 = None

        elif self.taille == (58,152):
            self.rect1.midbottom = (self.rect.centerx, self.rect.centery+80) 
            self.rect1.size = (58,76)
            self.rect2.midtop = (self.rect.centerx, self.rect.centery) 
            self.rect2.size = (58,76)
            self.rect3 = None
            self.rect4 = None
            self.rect5 = None
        
        elif self.taille == (174,76):
            self.rect1 = None
            self.rect2.midright = (self.rect.centerx + 80, self.rect.centery) 
            self.rect2.size = (58,76)
            self.rect3 = None
            self.rect4.center = (self.rect.centerx + 60, self.rect.centery) 
            self.rect4.size = (58,76)
            self.rect5.midleft = (self.rect.centerx + 20, self.rect.centery)
            self.rect5.size = (58,76)


    def test_rect1(self):
        #on crée une liste contenant les coordonnées x des centres des rectangles de l'arche
        list_center_x = [453, 513, 573, 633, 693, 753, 813]
        #on crée une liste contenant les coordonnées y des centres des rectangles de l'arche
        list_center_y = [225, 305, 385, 465]
        for i in list_center_x:
            for j in list_center_y:
                if abs(i - self.rect1.centerx) < 50 and abs(j - self.rect1.centery) < 70:
                    return True, i, j
        return False, None, None


    def test_rect2(self):
        list_center_x = [453, 513, 573, 633, 693, 753, 813]
        list_center_y = [225, 305, 385, 465]
        for i in list_center_x:
            for j in list_center_y:
                if abs(i - self.rect2.centerx) < 50 and abs(j - self.rect2.centery) < 70:
                    return True, i, j
        return False, None, None


    def test_rect3(self):
        list_center_x = [453, 513, 573, 633, 693, 753, 813]
        list_center_y = [225, 305, 385, 465]
        for i in list_center_x:
            for j in list_center_y:
                if abs(i - self.rect3.centerx) < 50 and abs(j - self.rect3.centery) < 70:
                    return True, i, j
        return False,None, None

    
    def test_rect4(self):
        list_center_x = [453, 513, 573, 633, 693, 753, 813]
        list_center_y = [225, 305, 385, 465]
        for i in list_center_x:
            for j in list_center_y:
                if abs(i - self.rect4.centerx) < 50 and abs(j - self.rect4.centery) < 70:
                    return True, i, j
        return False,None, None


    def test_rect5(self):
        list_center_x = [453, 513, 573, 633, 693, 753, 813]
        list_center_y = [225, 305, 385, 465]
        for i in list_center_x:
            for j in list_center_y:
                if abs(i - self.rect5.centerx) < 50 and abs(j - self.rect5.centery) < 70:
                    return True, i, j
        return False,None, None
