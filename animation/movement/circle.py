#FOR ENEMY MOVEMENT

import pygame as py
import math



BLACK=(0,0,0)
WHITE=(255,255,255)
FPS=600

py.init()
SCREEN=py.display.set_mode((800,800))
NAME=py.display.set_caption("Circal")
CLOCK=py.time.Clock()

T=0.5
t=0
xc=400
yc=400

paused=False
run=True

while run:
    SCREEN.fill(BLACK)
    
    
    
    for event in py.event.get():
        if event.type==py.QUIT:
            run=False
        if event.type==py.KEYDOWN:
            if event.key==py.K_SPACE:
                paused=not paused
                
    if not paused:
        t+=1 
        ang=int((2*3.14*t)/T)
        
        x=xc+100*math.cos(ang)
        y=yc+100*math.sin(ang)
        
        py.draw.circle(SCREEN,(WHITE),(x,y),5)
        py.display.flip()
    
    
    CLOCK.tick(FPS)
    
py.quit()

