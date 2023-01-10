import sys
import pygame
import config


class Ground(pygame.sprite.Sprite):
    def __init__(self, image, position):
        pygame.sprite.Sprite.__init__(self)

        # two same pictures
        self.image_0 = image
        self.rect_0 = self.image_0.get_rect()
        self.rect_0.left, self.rect_0.bottom = position

        self.image_1 = image
        self.rect_1 = self.image_1.get_rect()
        self.rect_1.left, self.rect_1.bottom = self.rect_0.right, self.rect_0.bottom

        # pixels move each term
        self.speed = -config.speed
        self.displacement = 0

    # calculate position
    def update(self):
        self.rect_0.left += self.speed
        self.rect_1.left += self.speed
        self.displacement -= self.speed
        if self.rect_0.right < 0:
            self.rect_0.left = self.rect_1.right
            self.rect_0, self.rect_1 = self.rect_1, self.rect_0

    # draw to screen
    def draw(self, screen):
        screen.blit(self.image_0, self.rect_0)
        screen.blit(self.image_1, self.rect_1)


class Cloud(pygame.sprite.Sprite):
    def __init__(self, image, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.speed = -config.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        self.rect.left += self.speed
        if self.rect.right < 0:
            self.kill()


class game_over(pygame.sprite.Sprite):
    def __init__(self, images, position):
        pygame.sprite.Sprite.__init__(self)
        self.images = images
        self.image = self.images[0]
        self.image_index = 0
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.centery = position

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        self.image = self.images[self.image_index]
        self.image_index += 1

        if self.image_index == len(self.images) - 2:
            self.image_index = len(self.images) - 3


class Moon(pygame.sprite.Sprite):
    def __init__(self, images, position):
        super().__init__()
        self.images = images
        self.image_index = 0
        self.image = self.images[self.image_index]
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.bottom = position
        self.refresh_counter = 0
        self.refresh_rate = 20

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        self.image = self.images[self.image_index]
        if self.refresh_counter == self.refresh_rate:
            self.image_index += 1
            if self.image_index == len(self.images):
                self.image_index = 7

            self.refresh_counter = 0
        self.refresh_counter += 1
        if self.image_index == 7:
            config.mode = 'day'

