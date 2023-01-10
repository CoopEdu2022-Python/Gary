import pygame
import sys
import config

class Dinosaur(pygame.sprite.Sprite):
    def __init__(self, images,audios,position):
        super().__init__()
        self.images = images
        self.audio = audios
        self.image = self.images[5]
        self.image_index = 5
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.bottom = position
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = 0
        self.refresh_rate = 10
        self.refresh_counter = 0
        self.duck_ = False
        self.dead_ = False
        self.jump_ = False
        self.statues = False
        self.movement = [0, 0]
        self.gravity = [0.1,0.7, 0.5]
        self.statue= config.game_status
    def start(self):
        self.statues = True





    def jump(self):
        if not self.duck_ and  not self.jump_:


            self.jump_ = True
            self.audio[0].play()
            self.movement[1] = -18


        else:
            return False

    def duck(self):
        if not self.jump_ :
            self.duck_ = True

    def un_duck(self):
        self.duck_ = False

    def die(self):
        if not self.dead_:

            self.audio[1].play()
            self.dead_ = True

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def load_image(self):
        self.image = self.images[self.image_index]
        rect = self.image.get_rect()
        rect.left, rect.top = self.rect.left, self.rect.top
        self.rect = rect
        self.mask = pygame.mask.from_surface(self.image)

    def refresh(self):
        if self.image_index == 5:
            self.image_index = 6
        elif self.image_index == 6:
            self.image_index = 5
        elif self.image_index == 2:
            self.image_index = 3
        elif self.image_index == 3:
            self.image_index = 2
        else:
            self.image_index = 0
        self.load_image()

    def update(self):
        if self.dead_:
            self.image_index = 4


        elif self.duck_:
            self.image_index = 2


        elif self.jump_:
            self.image_index = 4
            self.movement[1] += self.gravity[1]
            self.rect = self.rect.move(self.movement)
            self.statues = False
            if self.rect.bottom >= 295:
                self.rect.bottom = 295
                self.jump_ = False
                self.movement = [0, 0]
                self.image_index = 5

        elif self.statues:
            self.image_index = 7
        else:
            if self.refresh_counter == self.refresh_rate:
                self.refresh()
                self.refresh_counter = 0
            self.refresh_counter += 1

            self.rect.left += self.speed
        self.load_image()