import pygame as py
from menu import*

vec=py.math.Vector2
class Player(py.sprite.Sprite):
    def __init__ (self):
        super().__init__()
        py.init()
        
        self.img=py.image.load("images/curuma.png").convert_alpha()
        self.image=py.transform.scale(self.img,(120,120))
        
        self.rect=self.image.get_rect()
        
        self.pos=vec(WIDTH/2,HEIGHT/2)
        
        self.vel=vec(0,0)
        self.acc=vec(0,0)
        
    def update(self):
        self.acc=vec(0,0)
        keys = py.key.get_pressed()
        if keys[py.K_d] or keys[py.K_RIGHT]:
            self.acc.x = .5  # Acceleration on x-axis
        if keys[py.K_a] or keys[py.K_LEFT]:
            self.acc.x = -5 
            # Acceleration on y-axis
        if keys[py.K_w] or keys[py.K_UP]:
            self.acc.y = -.5  # Acceleration on x-axis
        if keys[py.K_s] or keys[py.K_DOWN]:
            self.acc.y= .5 
        if self.pos.x<0:
            self.pos.x=WIDTH
        if self.pos.x>WIDTH:
            self.pos.x=0
        if self.pos.y<0:
            self.pos.y=HEIGHT
        if self.pos.y>HEIGHT:
            self.pos.y=0
             
               
        self.acc+=self.vel * FRICTION     
        self.vel+=self.acc
        self.pos+=self.vel +0.5*self.acc
        
        self.rect.center=self.pos
    