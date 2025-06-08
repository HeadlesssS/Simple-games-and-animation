import pygame as py
from menu import*
from sprites import*
import random

class Game():
    def __init__(self):
        py.init()
        self.clock = py.time.Clock()
        py.mixer.init()
        self.SCREEN = py.display.set_mode((WIDTH, HEIGHT), py.RESIZABLE)
        icon = py.image.load("images/icon.jpg")
        self.strt_screen = py.image.load("images/actintro.jpg")
        self.scaledintro = py.transform.scale(self.strt_screen, (WIDTH, HEIGHT))
        ICON = py.display.set_icon(icon)
        
        GAME_NAME = py.display.set_caption("ORV")
        self.running = True
        
    def new(self):
        self.all_sprites = py.sprite.Group()
        self.platforms = py.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.platforms.add(p)
            self.all_sprites.add(p)
        self.run()

    def run(self):
        self.playing = True
        while self.playing:
            FPS = self.clock.tick(60)
            self.events()
            self.update()
            self.draw()
                
    def update(self):
        self.all_sprites.update()
        
        # Check if player hits a platform - only if falling
        if self.player.vel.y > 0:
            hits = py.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0
        
        # If player reaches top 1/4 of screen
        if self.player.rect.top <= HEIGHT / 4:
            self.player.pos.y += abs(self.player.vel.y)
            for plat in self.platforms:
                plat.rect.y += abs(self.player.vel.y)
                
        if self.player.rect.top > HEIGHT - 200:
            self.player.pos.y -= abs(self.player.vel.y)
            for plat in self.platforms:
                plat.rect.y -= abs(self.player.vel.y)
                
        # Ensure there are 12 platforms at every height
        section_height = HEIGHT // 12
        for i in range(12):
            section_top = i * section_height
            section_bottom = (i + 1) * section_height
            platforms_in_section = [plat for plat in self.platforms if section_top <= plat.rect.y < section_bottom]
            
            while len(platforms_in_section) < 1:
                width = random.randrange(50, 100)
                p = Platform(random.randrange(0, WIDTH - width), random.randrange(section_top, section_bottom), width, 20)
                self.platforms.add(p)
                self.all_sprites.add(p)
                platforms_in_section.append(p)
        
    def events(self):
        for event in py.event.get():
            if event.type == py.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
                py.quit()
                    
    def draw(self):
        self.SCREEN.fill(WHITE)
        self.all_sprites.draw(self.SCREEN)
        py.display.update()
            
    def show_start_screen(self):
        self.SCREEN.blit(self.scaledintro, (0, 0))
        py.display.flip()
        
    def show_GO_screen(self):
        pass
        
g = Game()

while g.running:
    g.show_start_screen() 
    g.clock.tick(FPS)
    g.new()
    g.show_GO_screen()
