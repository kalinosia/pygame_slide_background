import pygame, sys
import screen_file
import player_file
import title_file

import random
from pygame import mixer #??
import math
import time



pygame.init()
clock = pygame.time.Clock()



def update_fps():
    fps=clock.get_fps()
    #font = pygame.font.Font('freesansbold.ttf', 20)
    #text1=font.render(str(fps), True, (255,0,0))
    #screen.blit(text1, (0, 0))
    pygame.display.set_caption("2020   FPS: " + str(int(fps)))




titles=[]
player = player_file.Player(100, screen_file.screenY-200)
title = title_file.Title(screen_file.screenY-200)
titles.append(title)

#screen = pygame.display.set_mode((500, 500))

while True:
    clock.tick(60)
    #screen.fill((25,25,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            
            pygame.quit()
            sys.exit()

    screen_file.bg_pos_first, screen_file.bg_pos_second=screen_file.screen_update(screen_file.bg_pos_first, screen_file.bg_pos_second)
    update_fps()

    for title in titles:
        title.update()

        if not title.visible:
            titles.popleft()

    player.update()

    pygame.display.update()

