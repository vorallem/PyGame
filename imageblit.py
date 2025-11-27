import pygame
import time

pygame.init()
win = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Image Viewer")
state=1
x=640-270
y=320-270
image = pygame.image.load("images/tarunfinal.png")
bg = pygame.image.load("images/blissbg.jpg")


def redrawWindow():
    win.blit(bg,(0,0))
    win.blit(image,(x,y))
    pygame.display.update()

while state:
    time.sleep(0.00699300)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            state=0

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        print("SPACE PRESSED")
    redrawWindow()
pygame.quit()
