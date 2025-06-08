import pygame as py
import spritesheet

FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 255, 0)
GREEN = (0, 0, 255)
YELLOW = (255, 255, 0)

# Initialization
py.init()

SCREEN = py.display.set_mode((440, 440), py.RESIZABLE)
NAME = py.display.set_caption("dinosaur goes brrr")
CLOCK = py.time.Clock()

# Loading the sprite sheet
sprite_sheet_image = py.image.load("doux.png").convert_alpha()
sprite_sheet = spritesheet.Spritesheet(sprite_sheet_image)

# Create animation list
animation_list = []
animation_steps = [4, 6, 3, 4, 7]
action = 0
last_update = py.time.get_ticks()
animation_cooldown = 70
frame = 0
step_counter = 0

# Loop through each animation step
for animation in animation_steps:
    # Create a sublist for each animation step
    temp_list = []
    for _ in range(animation):
        # Append each frame to the sublist
        temp_list.append(sprite_sheet.get_image(step_counter, 24, 24, 3, (0, 0, 0)))
        step_counter += 1
    # Append the sublist to the main animation list
    animation_list.append(temp_list)
    

vel_y=0
jump_vel=-5
grav=1
ground=SCREEN.get_height()//2
cent=ground
jumping=False
run = True

while run:
    CLOCK.tick(FPS)
    

    SCREEN.fill(GREEN)
    
    
    for event in py.event.get():
        if event.type == py.QUIT:
            run = False

        if event.type == py.KEYDOWN:
            if event.key == py.K_DOWN and action > 0:
                action = 4
                frame = 0
                
            if event.key == py.K_UP  and jumping is False:
                print("sd")
                action = 2
                frame = 0
                jumping=True
                vel_y=jump_vel
            
    if jumping:
        cent+=vel_y
        vel_y+=grav
        
        if cent>=ground:
            jumping=False
            action=1
                
                
    current_time = py.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time
        if frame >= len(animation_list[action]):
            frame = 0

    # Blit the current frame of the current action
    SCREEN.blit(animation_list[action][frame], (0,cent))

    py.display.flip()

py.quit()
