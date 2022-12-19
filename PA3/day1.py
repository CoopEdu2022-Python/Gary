import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Hello World")
f = pygame.font.Font(None, 36)
text = f.render('Helloworld', True, (90, 0, 10), (1, 10, 80))
place = text.get_rect()
screen.blit(text, place)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
