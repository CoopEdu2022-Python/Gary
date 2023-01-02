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
    'pterodactyl': ['pterodactyl_1.png', 'pterodactyl_2.png'],

    'Cactus': ['Cactus_1.png', 'Cactus_2.png', 'Cactus_3.png', 'Cactus_4.png', 'Cactus_5.png', 'Cactus_6.png'],


}
pygame.init()
screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption(TITLE)
image_ground = pygame.image.load(IMAGE_PATHS['ground'])
ground = scene.Ground(image_ground, (0, SCREENSIZE[1]))
image_cloud = pygame.image.load(IMAGE_PATHS['cloud'])
clouds = pygame.sprite.Group()

image_pterodactyl = []
for i in range(2):
    image_pterodactyl.append(pygame.image.load(IMAGE_PATHS['pterodactyl'][i]))
image_Cactus = []
for i in range(6):
    image_Cactus.append(pygame.image.load(IMAGE_PATHS['Cactus'][i]))
pterodactyl = pygame.sprite.Group()

Cactus = pygame.sprite.Group()
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
    pterodactyl.draw(screen)
    pterodactyl.update()
    pygame.display.update()
    clock.tick(FPS)
