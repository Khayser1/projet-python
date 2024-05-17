import pygame
from Son import SoundManager

class bouton():
    def __init__(self,position_x,position_y,type_bouton,couleur_text,new_couleur,taille_police,position_text_x,position_text_y):
        self.image=pygame.image.load('/Users/nicolascastagni/Desktop/Jeu /Assets /test4.png')
        self.image=pygame.transform.scale(self.image,(200,115))
        self.bouton_rect=self.image.get_rect()
        self.bouton_rect.x=position_x
        self.bouton_rect.y=position_y
        self.font=pygame.font.Font('/Users/nicolascastagni/Desktop/Jeu /Assets /font.ttf',taille_police)
        self.couleur_text=couleur_text
        self.new_couleur_text=new_couleur
        self.type_bouton=type_bouton
        self.text=self.font.render(self.type_bouton,True,self.couleur_text)
        self.text_rect=self.text.get_rect()
        self.text_rect.x=position_text_x
        self.text_rect.y=position_text_y
        self.sound_manager=SoundManager()
        
        
    def update(self,surface):
       surface.blit(self.image,self.bouton_rect)
       
       
    def changement_couleur(self,surface):
        
        if self.bouton_rect.collidepoint(pygame.mouse.get_pos()):
           self.text= self.font.render(self.type_bouton,True,self.new_couleur_text)
        else:
            self.couleur_text=self.font.render(self.type_bouton,True,self.couleur_text)
        surface.blit(self.text,self.text_rect)
        
    
   