import pygame

pygame.init()
window = pygame.display.set_mode((1000, 1000))
rect1 = pygame.Rect(*window.get_rect().center, 0, 0).inflate(1, 1)
rect2 = pygame.Rect(0, 0, 75, 75)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    rect2.center = pygame.mouse.get_pos()
    collide = rect1.colliderect(rect2)
    
    window.fill(0)
    
    if collide:
        color = (255, 0, 0)
        pygame.draw.circle(window,(100,100,100),(500,500),100) 
        
    else:
        color=(255, 255, 255)

    
    pygame.draw.rect(window, color, rect1)
    pygame.draw.rect(window, (0, 255, 0), rect2, 6, 1)
    pygame.display.flip()

pygame.quit()
exit()
