import pygame as py
from menu import*

vec=py.math.Vector2

class Player(py.sprite.Sprite):
    def __init__ (self,game):
        py.sprite.Sprite.__init__(self)
        self.game=game
        self.img=py.image.load("images/ez.png").convert_alpha()
        self.image=py.transform.scale(self.img,(120,120))
        
        self.rect=self.image.get_rect()
        
        self.rect.center=(WIDTH/2,HEIGHT/2)
        self.pos=vec(WIDTH/2,HEIGHT/2)
        
        self.vel=vec(0,0)
        self.acc=vec(0,0)
        
    def update(self):
        self.acc=vec(0,0.8)
        keys = py.key.get_pressed()
        
        if keys[py.K_d] or keys[py.K_RIGHT]:
            self.acc.x = .4 # Acceleration on x-axis
        if keys[py.K_a] or keys[py.K_LEFT]:
            self.acc.x = -.4 
            # Acceleration on y-axis
        if keys[py.K_SPACE]:
            hits=py.sprite.spritecollide(self,self.game.platforms,False)
            if hits:self.vel.y-=20
            
        self.acc.x+=self.vel.x * FRICTION     
        self.vel+=self.acc
        self.pos+=self.vel +0.5*self.acc
        
        self.rect.midbottom=self.pos
    
    
class Platform(py.sprite.Sprite):
    def __init__ (self,x,y,w,h):
        py.sprite.Sprite.__init__(self)
        self.image=py.Surface((w,h))
        self.image.fill(BLUE)
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y