import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Hello World")
pygame.draw.rect(screen, (0, 0, 0), (0, 0, 640, 480))
pygame.draw.polygon(screen, (0, 0, 255), ((0, 0), (640, 0), (640, 480), (0, 480)))
pygame.draw.circle(screen, (255, 0, 0), (320, 240), 100)
pygame.draw.line(screen, (0, 255, 0), (0, 0), (640, 480), 5)
pygame.draw.ellipse(screen, (255, 255, 0), (100, 100, 200, 100))
pygame.draw.arc(screen, (255, 0, 255), (100, 100, 200, 100), 0, 3.14, 5)
pygame.draw.lines(screen, (0, 255, 255), True, ((100, 100), (200, 100), (200, 200), (100, 200)), 5)
pygame.draw.aaline(screen, (255, 255, 255), (100, 100), (200, 100))
pygame.draw.aalines(screen, (255, 255, 255), True, ((100, 100), (200, 100), (200, 200), (100, 200)))
while True:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()