import pygame as py
import math

class SineRectangle(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = py.Surface((40, 40))  # Rectangle size
        self.image.fill((255, 0, 0))  # Red color
        self.rect = self.image.get_rect()
        self.rect.center = (400, 400)  # Initial position (center of the screen)
        self.time = 0  # Initialize time for sine wave motion

    def update(self):
        # Update the position based on a sine wave
        self.time += 1
        self.rect.y = 200 + int(math.sin(self.time / 50.0) * 100)  # Adjust amplitude and frequency

class Game:
    def __init__(self):
        py.init()
        py.mixer.init()
        self.clock = py.time.Clock()
        self.screen = py.display.set_mode((800, 800), py.RESIZABLE)
        py.display.set_caption("Sine Wave")
        self.all_sprites = py.sprite.Group()  # Create a sprite group
        self.sine_rect = SineRectangle()  # Create the sine wave rectangle
        self.all_sprites.add(self.sine_rect)  # Add it to the sprite group

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(60)
            self.events()
            self.update()
            self.draw()

    def update(self):
        self.all_sprites.update()  # Update all sprites

    def events(self):
        for event in py.event.get():
            if event.type == py.QUIT:
                self.playing = False

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.all_sprites.draw(self.screen)  # Draw all sprites
        py.display.flip()

if __name__ == "__main__":
    g = Game()
    g.run()
    py.quit()
