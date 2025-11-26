import pygame
import time

pygame.init()
win = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Image Viewer")
state=1
x=640
y=320
width=50
height=50
while state:
    time.sleep(0.00699300)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            state=0

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        width+=2
    if keys[pygame.K_DOWN]:
        height+=2
    if keys[pygame.K_RIGHT] and width>=50: #conditions limitations boundaries
        width-=2
    if keys[pygame.K_LEFT] and height>=50: #conditions limitations boundaries
        height-=2
    win.fill((0,0,0))
    pygame.draw.rect(win,(255,255,255),((x-width/2),(y-height/2),width,height))
    pygame.display.update()
pygame.quit()
