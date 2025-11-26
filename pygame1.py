import pygame
import time

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Image Viewer")
state=1
while state:
    time.sleep(0.03)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            state=0
    
pygame.quit()
