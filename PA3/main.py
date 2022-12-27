import scene
import dinosaur
import obstacle
import random
import sys
import pygame

# settings
FPS = 60
TITLE = 'Chrome Dino'
BACKGROUND_COLOR = (235, 235, 235)
SCREENSIZE = (700, 300)
IMAGE_PATHS = {
    'ground': 'ground.png',
    'cloud': 'cloud.png',
    'pterodactyl': 'pterodactyl1.png',
    'pterodactyl2': 'pterodactyl2.png',
    'Cactus1': 'Cactus1.png',
    'Cactus2': 'Cactus2.png',
    'Cactus3': 'Cactus3.png',
    'Cactus4': 'Cactus4.png',
    'Cactus5': 'Cactus5.png',
    'Cactus6': 'Cactus6.png',

}
pygame.init()
screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption(TITLE)
image_ground = pygame.image.load(IMAGE_PATHS['ground'])
ground = scene.Ground(image_ground, (0, SCREENSIZE[1]))
image_cloud = pygame.image.load(IMAGE_PATHS['cloud'])
clouds = pygame.sprite.Group()
clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BACKGROUND_COLOR)
    if len(clouds) < 5:
        if random.randint(0, 100) <= 2:
            cloud = scene.Cloud(image_cloud, (SCREENSIZE[0], random.randint(0, 100)))
            clouds.add(cloud)
    elif len(clouds) > 5:
        clouds.empty()

    ground.draw(screen)
    ground.update()
    clouds.draw(screen)
    clouds.update()

    pygame.display.update()
    clock.tick(FPS)
