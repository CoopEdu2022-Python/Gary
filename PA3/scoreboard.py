import pygame
import os

import scene


class Scoreboard(pygame.sprite.Sprite):
    def __init__(self, images, position):
        pygame.sprite.Sprite.__init__(self)

        self.score = 0
        self.high_score = 0
        '''with open('high_score.txt', 'r') as f:
            self.high_score = int(f.read())'''

        self.images = images
        self.position = position
        self.image_score = self.rect_score = pygame.Surface((200, 100)).get_rect()
        self.image_high_score = self.rect_high_score = pygame.Surface((150, 100)).get_rect()
        self.refresh_rate = 20
        self.refresh_counter = 0

    def update(self):
        # stitch current score image
        self.image_score = pygame.Surface((20 * 5, 31))
        self.rect_score = self.image_score.get_rect()
        self.rect_score.right, self.rect_score.top = self.position
        for i, y in enumerate(str(self.score).zfill(5)):  # current score images

            self.image_score.blit(self.images[int(y)], (20 * i, 0))

        # stitch high score image
        self.image_high_score = pygame.Surface((60 + 20 * 5, 31))
        self.image_high_score.blit(self.images[-1], (0, 0))
        for i, _ in enumerate(str(self.high_score).zfill(5)):  # highest score images
            self.image_high_score.blit(self.images[int(_)], (60 + 20 * i, 0))

    def draw(self, screen):
        screen.blit(self.image_score, self.rect_score)
