import scene
import dinosaur
import obstacle
import random
import sys
import pygame
import scoreboard
import config
# settings


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode(config.SCREENSIZE)
pygame.display.set_caption(config.TITLE)
image_ground = pygame.image.load(config.IMAGE_PATHS['ground'])
ground = scene.Ground(image_ground, (0, config.SCREENSIZE[1]))
image_cloud = pygame.image.load(config.IMAGE_PATHS['cloud'])
clouds = pygame.sprite.Group()

clock = pygame.time.Clock()

image_pterodactyl = []
for i in range(2):
    image_pterodactyl.append(pygame.image.load(config.IMAGE_PATHS['pterodactyl'][i]))

pterodactyl = pygame.sprite.Group()
image_cactus = []
for i in range(6):
    image_cactus.append(pygame.image.load(config.IMAGE_PATHS['Cactus'][i]))
Cactus = pygame.sprite.Group()
image_dinosaur = []
for i in range(8):
    image_dinosaur.append(pygame.image.load(config.IMAGE_PATHS['dinosaur'][i]))
audio_dinosaur = []
for i in range(3):
    audio_dinosaur.append(pygame.mixer.music.load(config.AUDIO_PATHS['dinosaur'][i]))

dinosaur = dinosaur.Dinosaur(image_dinosaur, audio_dinosaur, (100, 295))
image_score_board = []

for i in range(11):
    image_score_board.append(pygame.image.load(config.IMAGE_PATHS['score_board'][i]))
score_board = scoreboard.Scoreboard(image_score_board, (100, 50))
game_status = 'start'

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
        clock.tick(config.FPS)


def end():
    global game_status
    while game_status == 'end':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_status = 'quit'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_status = 'start'
        screen.fill((255, 255, 255))

        pygame.display.update()
        clock.tick(60)
        config.speed =0


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

    screen.fill(config.BACKGROUND_COLOR)

    if len(clouds) < 5:
        if random.randint(0, 100) <= 2:
            cloud = scene.Cloud(image_cloud, (config.SCREENSIZE[0], random.randint(0, 100)))
            clouds.add(cloud)
    elif len(clouds) > 5:
        clouds.empty()
    if len(pterodactyl) < 2:
        if random.randint(0, 100) <= 1:
            pterodactyl_ = obstacle.Pterodactyl(image_pterodactyl, (config.SCREENSIZE[0], random.choice([200, 175, 150])))
            pterodactyl.add(pterodactyl_)
    elif len(pterodactyl) > 2:
        pterodactyl.empty()
    if len(Cactus) < 3:
        if random.randint(0, 100) <= 2:
            cactus = obstacle.Cactus(image_cactus, (config.SCREENSIZE[0], 295))
            Cactus.add(cactus)
    elif len(Cactus) > 3:
        Cactus.empty()
    pygame.sprite.groupcollide(Cactus, pterodactyl, False, True)
    if pygame.sprite.spritecollide(dinosaur, Cactus, False) or pygame.sprite.spritecollide(dinosaur, pterodactyl,
                                                                                           False):
        dinosaur.die()

    # scoreboard
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
    score_board.update()
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
    clock.tick(config.FPS)
    # update score
