import pygame as py
import os 

# Constants
HEIGHT = 800
WIDTH = 600
WHITE = (255, 255, 255)
run = True

# Jump variables
is_jumping = False
is_ajumping=False
jump_force = 15
gravity = 1
velocity_y = 0

# Initialize the screen
py.init()
clock = py.time.Clock()
SCREEN = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("game")

sprite_folder = "png"
animations = {
    "attack": [],
    "dead": [],
    "idle": [],
    "jump": [],
    "JumpAttack": [],
    "run": [],
    "walk": []
}
# Load images for each animation
for animation in animations.keys():
    for i in range(10):
        image_path = os.path.join(sprite_folder, f"{animation} ({i+1}).png")
        if os.path.exists(image_path):
            image = py.image.load(image_path).convert_alpha()
            image = py.transform.scale(image, (72, 72))
            player_rect = image.get_rect()
            player_rect.center = (WIDTH / 2, HEIGHT / 2)
            
            animations[animation].append(image)
        else:
            print(f"Image not found: {image_path}")

frame_index = 0


def animate(animation):
    global frame_index
    if animation in animations:
        sp = animations[animation][frame_index]
        SCREEN.blit(sp, (player_rect.x, player_rect.y))
        frame_index = (frame_index + 1) % len(animations[animation])
    else:
        print(f"Animation '{animation}' not found")

while run:
    current_animation = "idle"
    SCREEN.fill(WHITE)
    
    for event in py.event.get():
        if event.type == py.QUIT:
            run = False
    
    keys = py.key.get_pressed()
    if keys[py.K_SPACE]:
        current_animation = "attack"
    elif keys[py.K_x]:
        current_animation = "dead"
    elif keys[py.K_s]:
        current_animation = "idle"
    elif keys[py.K_w] and not is_jumping:
        
        is_jumping = True
        velocity_y = -jump_force
    elif keys[py.K_j]and not is_ajumping:
        current_animation = "JumpAttack"
        is_ajumping=True
        velocity_y=-jump_force
    elif keys[py.K_d]:
        current_animation = "run"
        player_rect.x += 6
    elif keys[py.K_a]:
        current_animation = "walk"
        player_rect.x -= 3
      # Default animation
    # Apply gravity
    if is_jumping:
        current_animation = "jump"
        player_rect.y += velocity_y
        velocity_y += gravity
        if player_rect.y >= HEIGHT / 2:  # Assuming ground level is at HEIGHT / 2
            player_rect.y = HEIGHT / 2
            is_jumping = False
            velocity_y = 0
    if is_ajumping:
        current_animation = "JumpAttack"
        player_rect.y += velocity_y
        velocity_y += gravity
        if player_rect.y >= HEIGHT / 2:  # Assuming ground level is at HEIGHT / 2
            player_rect.y = HEIGHT / 2
            is_ajumping = False
            velocity_y = 0

    # Boundary check
    if player_rect.x < 0:
        player_rect.x = 0
    elif player_rect.x > WIDTH - player_rect.width:
        player_rect.x = WIDTH - player_rect.width
    if player_rect.y < 0:
        player_rect.y = 0
    elif player_rect.y > HEIGHT - player_rect.height:
        player_rect.y = HEIGHT - player_rect.height
    
    
    animate(current_animation)
    py.display.flip()
    clock.tick(10)  # Adjust animation speed

py.quit()
