import pygame
import screen_file


class Player():
    def __init__(self, x, y):
        self.img_walk = []
        self.img_run = []
        self.img_jump = []
        self.img_dead = []
        for num in range(1, 16):
            #imahe size is 614 x 564 ,so 307,282 or ??
            #buy really this is size dead so toch is about ~250/300 [230 head] so it's 37,5% width is real width
            sizeXmg, sizeYimg=122, 112
            img = pygame.image.load(f'img/guy/Walk ({num}).png')
            img = pygame.transform.scale(img, (sizeXmg, sizeYimg))#????rozmiar ludzika
            self.img_walk.append(img)
            img = pygame.image.load(f'img/guy/Run ({num}).png')
            img = pygame.transform.scale(img, (sizeXmg, sizeYimg))  # ????rozmiar ludzika
            self.img_run.append(img)
            img = pygame.image.load(f'img/guy/Jump ({num}).png')
            img = pygame.transform.scale(img, (sizeXmg, sizeYimg))  # ????rozmiar ludzika
            self.img_jump.append(img)
            img = pygame.image.load(f'img/guy/Dead ({num}).png')
            img = pygame.transform.scale(img, (sizeXmg, sizeYimg))  # ????rozmiar ludzika
            self.img_dead.append(img)
        self.index = 0
        self.image = self.img_run[self.index]
        self.rect = self.image.get_rect()
        self.width = self.image.get_width()#dont need
        self.rect.x = x
        self.rect.y = y
        self.vel_y = 0
        self.jumped = False
        self.jumping = False
        self.walking = True
        self.running = False
        self.ileklatek = 0

    def update(self):
        dx = 0
        dy = 0
        #print(self.rect.right)
        # get keypresses
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.jumped == False and not self.jumping:
            self.vel_y = -15
            self.jumped = True
            self.jumping = True
            self.walking=False
            self.running=False
            #self.ileklatek = 0
            self.index=0
        #if key[pygame.K_SPACE] and self.jumped == False and self.jumping and colision:
        #    you can jump
        if key[pygame.K_SPACE] == False:
            self.jumped = False
        if key[pygame.K_LEFT] and not self.jumping:
            dx -= 5
            self.index -= 1
        if key[pygame.K_RIGHT]:
            dx += 5
            if self.walking:
                self.walking = False
                self.index = 0
                self.running = True
        if not key[pygame.K_RIGHT] and self.running:
            self.running = False
            self.index = 0
            self.walking = True
        '''
        if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
            self.counter = 0
            self.index = 0
            if self.direction == 1:
                self.image = self.images_right[self.index]
            if self.direction == -1:
                self.image = self.images_left[self.index]
        '''
        # handle animation
        self.index += 1
        if self.index >= 28 and self.jumping:
            self.index = 0
            self.jumping = False
            self.walking = True    ########
        elif self.index >= 15 and not self.jumping:
            self.index = 0

        if self.walking:
            self.image = self.img_walk[self.index]
        elif self.running:
            self.image = self.img_run[self.index]
        elif self.jumping:
            index=self.index/2
            index=int(index)
            #print("index", index)
            self.image = self.img_jump[index]
        '''
        if self.direction == 1:
            self.image = self.images_right[self.index]
        if self.direction == -1:
            self.image = self.images_left[self.index]
        '''
        ## add gravity
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y

        # check for collision

        # update player coordinates
        self.rect.x += dx
        self.rect.y += dy

        #how hight run our boy
        if self.rect.bottom > screen_file.screenY-(0.01*screen_file.screenY):
            self.rect.bottom = screen_file.screenY-(0.01*screen_file.screenY)
            dy = 0

        #you can't run beyond screen
        if self.rect.x<0:
            self.rect.x=0
        if self.rect.x+self.width>screen_file.screenX:
            self.rect.x=screen_file.screenX-self.width

        #ile klatek skacze
        #if self.rect.bottom<screen_file.screenY-100:
        #    print(self.ileklatek)
        #    self.ileklatek+=1

        # draw player onto screen
        screen_file.screen.blit(self.image, self.rect)
