import pygame


class SoundManager:
    def __init__(self):
        self.click=pygame.mixer.Sound("/Users/nicolascastagni/Desktop/Jeu /Assets /click.mp3")
        
    def click(self):
        self.click.play()
        
    
         