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
SCREENSIZE = (1200, 300)
IMAGE_PATHS = {
    'ground': r'C:\Users\zhang\PycharmProjects\homework\PA3\ground\ground.png',
    'cloud': r'C:\Users\zhang\PycharmProjects\homework\PA3\cloud\cloud.png',
    'pterodactyl': [r'C:\Users\zhang\PycharmProjects\homework\PA3\pterodactyl/pterodactyl-1.png',
                    r'C:\Users\zhang\PycharmProjects\homework\PA3\pterodactyl\pterodactyl-2.png'],

    'Cactus': [r'C:\Users\zhang\PycharmProjects\homework\PA3\cactus\cactus-1.png',
               r'C:\Users\zhang\PycharmProjects\homework\PA3\cactus\cactus-2.png',
               r'C:\Users\zhang\PycharmProjects\homework\PA3\cactus\cactus-3.png',
               r'C:\Users\zhang\PycharmProjects\homework\PA3\cactus\cactus-4.png',
               r'C:\Users\zhang\PycharmProjects\homework\PA3\cactus\cactus-2.png',
               r'C:\Users\zhang\PycharmProjects\homework\PA3\cactus\cactus-2.png'],
    'dinosaur': [r'C:\Users\zhang\PycharmProjects\homework\PA3\dinosaur\dinosaur-die-1.png',
                 r'C:\Users\zhang\PycharmProjects\homework\PA3\dinosaur\dinosaur-die-2.png',
                 r'C:\Users\zhang\PycharmProjects\homework\PA3\dinosaur\dinosaur-duck-1.png',
                 r'C:\Users\zhang\PycharmProjects\homework\PA3\dinosaur\dinosaur-duck-2.png',
                 r'C:\Users\zhang\PycharmProjects\homework\PA3\dinosaur\dinosaur-jump.png',
                 r'C:\Users\zhang\PycharmProjects\homework\PA3\dinosaur\dinosaur-run-1.png',
                 r'C:\Users\zhang\PycharmProjects\homework\PA3\dinosaur\dinosaur-run-2.png',
                 r'C:\Users\zhang\PycharmProjects\homework\PA3\dinosaur\dinosaur-start.png',
                 r'C:\Users\zhang\PycharmProjects\homework\PA3\dinosaur\dinosaur-unknown-1.png']

}
AUDIO_PATHS = {}

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

pterodactyl = pygame.sprite.Group()
image_cactus = []
for i in range(6):
    image_cactus.append(pygame.image.load(IMAGE_PATHS['Cactus'][i]))
image_dinosaur = []
for i in range(8):
    image_dinosaur.append(pygame.image.load(IMAGE_PATHS['dinosaur'][i]))

Cactus = pygame.sprite.Group()
clock = pygame.time.Clock()
dinosaur = dinosaur.Dinosaur(image_dinosaur, (100, 295))
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                dinosaur.jump()
            elif event.key == pygame.K_DOWN:
                dinosaur.duck()
        elif event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
            dinosaur.un_duck()

    screen.fill(BACKGROUND_COLOR)

    if len(clouds) < 5:
        if random.randint(0, 100) <= 2:
            cloud = scene.Cloud(image_cloud, (SCREENSIZE[0], random.randint(0, 100)))
            clouds.add(cloud)
    elif len(clouds) > 5:
        clouds.empty()
    if len(pterodactyl) < 2:
        if random.randint(0, 100) <= 1:
            pterodactyl_ = obstacle.Pterodactyl(image_pterodactyl, (SCREENSIZE[0], random.choice([200, 175, 150])))
            pterodactyl.add(pterodactyl_)
    elif len(pterodactyl) > 2:
        pterodactyl.empty()
    if len(Cactus) < 3:
        if random.randint(0, 100) <= 2:
            cactus = obstacle.Cactus(image_cactus, (SCREENSIZE[0], 295))
            Cactus.add(cactus)
    elif len(Cactus) > 3:
        Cactus.empty()
    pygame.sprite.groupcollide(Cactus, pterodactyl, False,True)
#    if pygame.sprite.spritecollide(dinosaur, Cactus, False) or pygame.sprite.spritecollide(dinosaur, pterodactyl, False):
#        dinosaur.die()
    dinosaur.draw(screen)
    dinosaur.update()

    ground.draw(screen)
    ground.update()
    clouds.draw(screen)
    clouds.update()
    pterodactyl.draw(screen)
    pterodactyl.update()
    Cactus.draw(screen)
    Cactus.update()
    pygame.display.update()
    clock.tick(FPS)
