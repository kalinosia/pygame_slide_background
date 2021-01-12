import pygame
import time

#background are 1920 x 1080
# wewant half and not that high (half) so H:540 and width on half (/4) W:480
screenX=960
screenY=540
screen = pygame.display.set_mode((screenX, screenY))
#pygame.display.set_caption("Xmas Time To Game")
#screen.fill((25,25,255))
background=[]
for num in range(1, 5):
    img = pygame.image.load(f'img/background{num}.png').convert()  # conxert to faster work?
    img = pygame.transform.scale(img, (screenX, screenY))
    background.append(img)
#background = pygame.image.load('img/background.png').convert() #conxert to faster work?
#background = pygame.transform.scale(background, (screenX*2, screenY))
bg_pos_first=0
bg_pos_second=screenX


def screen_update(bg_pos_first, bg_pos_second):
    bg_pos_first-=1
    bg_pos_second-=1

    if bg_pos_first == -screenX:
        bg_pos_first=screenX
    elif bg_pos_second==-screenX:
        bg_pos_second=screenX

    screen.blit(background[0], (bg_pos_first, 0))
    screen.blit(background[0], (bg_pos_second, 0))
    return bg_pos_first, bg_pos_second
