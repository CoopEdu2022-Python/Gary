import scene
import dinosaur
import obstacle
import random
import sys
import pygame
import scoreboard

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
                 r'C:\Users\zhang\PycharmProjects\homework\PA3\dinosaur\dinosaur-unknown-1.png', ],
    'score_board': [r'C:\Users\zhang\PycharmProjects\homework\PA3\scoreboard\scoreboard-0.png',
                    r'C:\Users\zhang\PycharmProjects\homework\PA3\scoreboard\scoreboard-1.png',
                    r'C:\Users\zhang\PycharmProjects\homework\PA3\scoreboard\scoreboard-2.png',
                    r'C:\Users\zhang\PycharmProjects\homework\PA3\scoreboard\scoreboard-3.png',
                    r'C:\Users\zhang\PycharmProjects\homework\PA3\scoreboard\scoreboard-4.png',
                    r'C:\Users\zhang\PycharmProjects\homework\PA3\scoreboard\scoreboard-5.png',
                    r'C:\Users\zhang\PycharmProjects\homework\PA3\scoreboard\scoreboard-6.png',
                    r'C:\Users\zhang\PycharmProjects\homework\PA3\scoreboard\scoreboard-7.png',
                    r'C:\Users\zhang\PycharmProjects\homework\PA3\scoreboard\scoreboard-8.png',
                    r'C:\Users\zhang\PycharmProjects\homework\PA3\scoreboard\scoreboard-9.png',
                    r'C:\Users\zhang\PycharmProjects\homework\PA3\scoreboard\scoreboard-10.png', ]

}
AUDIO_PATHS = {'dinosaur': [r'C:\Users\zhang\PycharmProjects\homework\PA3\jump.mp3',
                            r'C:\Users\zhang\PycharmProjects\homework\PA3\music.mp3',
                            r'C:\Users\zhang\PycharmProjects\homework\PA3\score.mp3']}

pygame.init()
pygame.mixer.init()
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
Cactus = pygame.sprite.Group()
image_dinosaur = []
for i in range(8):
    image_dinosaur.append(pygame.image.load(IMAGE_PATHS['dinosaur'][i]))
audio_dinosaur = []
for i in range(3):
    audio_dinosaur.append(pygame.mixer.music.load(AUDIO_PATHS['dinosaur'][i]))

dinosaur = dinosaur.Dinosaur(image_dinosaur, audio_dinosaur, (100, 295))
image_score_board = []
score_board = scoreboard.Scoreboard(image_score_board, (100, 50))
for i in range(11):
    image_score_board.append(pygame.image.load(IMAGE_PATHS['score_board'][i]))

game_status = 'start'
clock = pygame.time.Clock()
def start():
    global game_status
    while game_status == 'start':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_status = 'quit'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_status = 'running'
        screen.fill((255, 255, 255))
        screen.blit(image_dinosaur[8], (100, 295))
        pygame.display.update()
        clock.tick(60)
while True:

    for event in pygame.event.get():
        if game_status == 'play':
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
    pygame.sprite.groupcollide(Cactus, pterodactyl, False, True)
    if pygame.sprite.spritecollide(dinosaur, Cactus, False) or pygame.sprite.spritecollide(dinosaur, pterodactyl,
                                                                                           False):
        dinosaur.die()
    score_board.score = ground.displacement // 50  # algorithm of score
    if score_board.score and not score_board.score % 100:
        pygame.mixer.Sound(r'C:\Users\zhang\PycharmProjects\homework\PA3\score.mp3').play()  # sound
    if game_status == 'end':
        score_board.high_score = max(score_board.score, score_board.high_score)
        with open('score.txt', 'w') as f:
            f.write(str(score_board.high_score))

    dinosaur.update()
    dinosaur.draw(screen)
    dinosaur.update()
    score_board.draw(screen)
    ground.update()
    ground.draw(screen)
    clouds.update()
    clouds.draw(screen)
    clouds.update()
    pterodactyl.draw(screen)
    Cactus.update()
    Cactus.draw(screen)

    pygame.display.update()
    clock.tick(FPS)
    # update score
