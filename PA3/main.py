import scene
import dinosaur
import obstacle
import random
import sys
import pygame
import scoreboard
import config
import time

# settings


pygame.init()

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
    audio_dinosaur.append(pygame.mixer.Sound(config.AUDIO_PATHS['dinosaur'][i]))

dinosaur = dinosaur.Dinosaur(image_dinosaur, audio_dinosaur, (100, 295))
image_score_board = []

for i in range(20):
    image_score_board.append(pygame.image.load(config.IMAGE_PATHS['score_board'][i]))
score_board = scoreboard.Scoreboard(image_score_board, (600, 1500))
image_game_over = []
for i in range(9):
    image_game_over.append(pygame.image.load(config.IMAGE_PATHS['end'][i]))
game_over = scene.game_over(image_game_over, (600, 150))
game_status = config.game_status


def start():
    global game_status
    if game_status == 'start':

        clock = pygame.time.Clock()
        press = False

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                        dinosaur.jump()
                        press = True

                else:
                    dinosaur.start()

            screen.fill(config.BACKGROUND_COLOR)
            dinosaur.update()
            dinosaur.draw(screen)
            pygame.display.update()
            clock.tick(config.FPS)
            config.speed = 0
            if press and not dinosaur.jump_:
                game_status = 'running'
                return True


def end():
    global game_status
    while game_status == 'end':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    config.game_status = 'start'
                    return True
        clock = pygame.time.Clock()
        game_over.draw(screen)
        game_over.update()
        time.sleep(0.5)
        pygame.display.update()

        config.speed = 0
        clock.tick(config.FPS)

def running():
    while True:

        for event in pygame.event.get():
            if config.game_status == 'running':
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
        config.speed = 10
        screen.fill(config.BACKGROUND_COLOR)
        # scoreboard
        score_board.score = ground.displacement // 50  # algorithm of score
        if score_board.score and not score_board.score % 100:
            pygame.mixer.Sound(r'C:\Users\zhang\PycharmProjects\homework\PA3\score.mp3').play()
            config.speed += 0.5

        if config.game_status == 'end':
            score_board.high_score = max(score_board.score, score_board.high_score)
            with open('score.txt', 'w') as f:
                f.write(str(score_board.high_score))
        if dinosaur.dead_:
            return True

        if len(clouds) < 5:
            if random.randint(0, 100) <= 2:
                cloud = scene.Cloud(image_cloud, (config.SCREENSIZE[0], random.randint(0, 100)))
                clouds.add(cloud)
        elif len(clouds) > 5:
            clouds.empty()
        if len(pterodactyl) < 2 and score_board.score > 200:
            if random.randint(0, 100) <= 2:
                pterodactyl_ = obstacle.Pterodactyl(image_pterodactyl,
                                                    (config.SCREENSIZE[0], random.choice([200, 175, 150])))
                pterodactyl.add(pterodactyl_)
        elif len(pterodactyl) > 2:
            pterodactyl.empty()
        if len(Cactus) < 3 and score_board.score > 100:
            if random.randint(0, 100) <= 2:
                cactus = obstacle.Cactus(image_cactus, (config.SCREENSIZE[0], 295))
                Cactus.add(cactus)
        elif len(Cactus) > 3:
            Cactus.empty()
        pygame.sprite.groupcollide(Cactus, pterodactyl, False, True)
        if pygame.sprite.spritecollide(dinosaur, Cactus, False) or pygame.sprite.spritecollide(dinosaur, pterodactyl,
                                                                                               False):
            dinosaur.die()
            config.game_status = 'end'
        if score_board.score % 1000 == 0:
            config.mode = 'night'
            if config.mode == 'night':
                config.screen_color_rate -= 1
                if config.screen_color_rate <= 0:

                    config.screen_color_rate += 1
                    if config.screen_color_rate >= 255:
                        config.screen_color_rate = 255
                        config.mode = 'day'
                config.screen_color = (config.screen_color_rate, config.screen_color_rate, config.screen_color_rate)
                screen.fill(config.screen_color)
        score_board.update()
        score_board.draw(screen)
        dinosaur.update()
        dinosaur.draw(screen)
        dinosaur.update()

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


while True:
    if start():
        config.game_status = 'running'
        if running():
            if end():
                continue
