import pygame as py
from menu import*
from sprites import*

class Game():
    def __init__(self):
        py.init()
        self.clock=py.time.Clock()
        py.mixer.init()
        self.SCREEN=py.display.set_mode((WIDTH,HEIGHT),py.RESIZABLE)
        icon=py.image.load("images/icon.jpg")
        self.strt_screen=py.image.load("images/actintro.jpg")
        self.scaledintro=py.transform.scale(self.strt_screen,(WIDTH,HEIGHT))
        ICON= py.display.set_icon(icon)
        
        GAME_NAME=py.display.set_caption("ORV")
        self.run=True
        
    def new(self):
            self.all_sprites=py.sprite.Group()
            self.player=Player()
            self.all_sprites.add(self.player)
            g.runs()
        
    def runs(self):
            self.playing=True
            while self.playing:
                FPS=self.clock.tick(60)
                self.events()
                self.update()
                self.draw()
                
    def update(self):
            self.player.update()
            self.all_sprites.update()
        
    def events(self):
            for event in py.event.get():
                if event.type==py.QUIT:
                    if self.playing:
                        self.playing=False
                    self.run=False
                    
        
    def draw(self):
            self.SCREEN.fill(WHITE)
            self.all_sprites.draw(self.SCREEN)
            py.display.update()
            
        
    def show_start_screen(self):
            self.SCREEN.blit(self.scaledintro,(0,0))
            py.display.flip()
        
    def show_GO_screen(self):
            pass
        
g=Game()

while g.run:
    g.show_start_screen()
    
    g.new()
    g.show_GO_screen()