import pygame as py
from pygame.locals import *
from sys import exit

py.init()
screen_size=(640,480)
screen=py.display.set_mode(screen_size,0,32)

font=py.font.SysFont("arial",16)
font_height=font.get_linesize()
event_text=[]

while True:
    event=py.event.wait()
    event_text.append(str(event))
    event_text=event_text[-int(screen_size[1]/font_height): ]
    
    if event.type==QUIT:
        exit()
    screen.fill((255,255,255))
    
    y=screen_size[1]-font_height
    for text in reversed(event_text):
        screen.blit(font.render(text,True,(0,255,0)),(0,y))
        y-=font_height
    py.display.update()
