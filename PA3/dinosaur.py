import pygame
import sys


class Dinosaur(pygame.sprite.Sprite):
    def __init__(self, images, position):
        super().__init__()
        self.images = images
        self.image = self.images[5]
        self.image_index = 5
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.bottom = position
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = 0
        self.refresh_rate = 10
        self.refresh_counter = 0
        self.duck = False
        self.dead = False
        self.jump = False

    def jump(self):
        if not self.jump and not self.duck and not self.dead:
            self.jump = True

            self.rect = self.rect.move([0, -self.speed])

        else:
            return

    def duck(self):
        if not self.duck and not self.jump and not self.dead:
            self.duck = True
            self.rect = self.rect.move([0, self.speed])
        else:
            return

    def un_duck(self):
        self.duck = False

    def die(self):
        if not self.dead:
            self.dead = True
        else:
            return

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
        else:
            self.image_index = 0
        self.load_image()

    def update(self):
        if self.dead:
            self.image_index = 4
            self.load_image()
            return
        elif self.duck:
            self.image_index = 1
            self.load_image()
            return
        elif self.jump:
            self.image_index = 2
            self.load_image()
            return
        else:
            if self.refresh_counter == self.refresh_rate:
                self.refresh()
                self.refresh_counter = 0
            self.refresh_counter += 1

            self.rect.left += self.speed
