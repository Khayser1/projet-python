import pygame as pg
class Arche:
    def __init__(self, points):
        self.points = points
        self.pieces = []
arche_point = [(0,0),(100,0),(150,50),(100,100),(0,100)]
BLUE = [0,0,255]
pg.draw.polygon(BLUE, arche_point)