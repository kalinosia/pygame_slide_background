import pygame
import screen_file


class Title():
    def __init__(self, y):
        self.img = pygame.image.load('img/paddle.png')
        self.img = pygame.transform.scale(self.img, (int(self.img.get_width()/3), int(self.img.get_height()/3)))#????rozmiar paddle
        self.rect = self.img.get_rect()
        self.rect.x = screen_file.screenX
        self.rect.y = y

    def update(self):
        dx = 0
        dy = 0
        self.visible=True
        
        dx-=1

        self.rect.x += dx
        self.rect.y += dy
        
        if self.rect.left < 0:#########
            self.visible=False
        if self.rect.bottom>screen_file.screenX:
            self.visible=False

        # draw player onto screen
        screen_file.screen.blit(self.img, self.rect)