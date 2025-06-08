#FOR ENEMY MOVEMENT

import pygame as py
import math



BLACK=(0,0,0)
WHITE=(255,255,255)
FPS=60

py.init()
SCREEN=py.display.set_mode((800,800))
CLOCK=py.time.Clock()


x=0

run=True
while run:
    
    x+=1
    
    y=200+int(math.tan(x/100)*100)
    
    for event in py.event.get():
        if event.type==py.QUIT:
            run=False
            
    if x>800:
        x=0
    
    rect=py.Rect(x,y,10,10)
    py.draw.rect(SCREEN,WHITE,rect)
    
    py.display.flip()
    
    
    CLOCK.tick(FPS)
    
py.quit()

