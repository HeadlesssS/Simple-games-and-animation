import pygame as py

py.init()
t = py.time.Clock()

SCREEN = py.display.set_mode()
width, height = SCREEN.get_size()

COLOR = [ (255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255),(122,122,122)]

def draw_square(length, num):
    
    rect = py.Rect(width // 2, height // 2, length, length)
    py.draw.rect(SCREEN, COLOR[num], rect, 1)
    py.display.update()
    

x = 0
y = 1
sum = 0
run = True
i = 0
while run:
    sum = x + y

    if i >=len(COLOR)-1:
        i = 0
        
    draw_square(sum, int(i))
    x = y
    y = sum
    t.tick(0.9)

    for event in py.event.get():
        if event.type == py.QUIT:
            run = False
    i += 1

py.quit()
