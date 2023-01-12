import pygame

speed = 10
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
    'score_board': [[r'C:\Users\zhang\PycharmProjects\homework\PA3\scoreboard\scoreboard-0.png',
                     r'C:\Users\zhang\PycharmProjects\homework\PA3\scoreboard\scoreboard-1.png',
                     r'C:\Users\zhang\PycharmProjects\homework\PA3\scoreboard\scoreboard-2.png',
                     r'C:\Users\zhang\PycharmProjects\homework\PA3\scoreboard\scoreboard-3.png',
                     r'C:\Users\zhang\PycharmProjects\homework\PA3\scoreboard\scoreboard-4.png',
                     r'C:\Users\zhang\PycharmProjects\homework\PA3\scoreboard\scoreboard-5.png',
                     r'C:\Users\zhang\PycharmProjects\homework\PA3\scoreboard\scoreboard-6.png',
                     r'C:\Users\zhang\PycharmProjects\homework\PA3\scoreboard\scoreboard-7.png',
                     r'C:\Users\zhang\PycharmProjects\homework\PA3\scoreboard\scoreboard-8.png',
                     r'C:\Users\zhang\PycharmProjects\homework\PA3\scoreboard\scoreboard-9.png',
                     r'C:\Users\zhang\PycharmProjects\homework\PA3\scoreboard\scoreboard-10.png'],
                    [r'C:\Users\zhang\PycharmProjects\homework\PA3\scoreboard\scoreboard-0.png',
                     r'C:\Users\zhang\PycharmProjects\homework\PA3\scoreboard\scoreboard-1.png',
                     r'C:\Users\zhang\PycharmProjects\homework\PA3\scoreboard\scoreboard-2.png',
                     r'C:\Users\zhang\PycharmProjects\homework\PA3\scoreboard\scoreboard-3.png',
                     r'C:\Users\zhang\PycharmProjects\homework\PA3\scoreboard\scoreboard-4.png',
                     r'C:\Users\zhang\PycharmProjects\homework\PA3\scoreboard\scoreboard-5.png',
                     r'C:\Users\zhang\PycharmProjects\homework\PA3\scoreboard\scoreboard-6.png',
                     r'C:\Users\zhang\PycharmProjects\homework\PA3\scoreboard\scoreboard-7.png',
                     r'C:\Users\zhang\PycharmProjects\homework\PA3\scoreboard\scoreboard-8.png',
                     r'C:\Users\zhang\PycharmProjects\homework\PA3\scoreboard\scoreboard-9.png',
                     r'C:\Users\zhang\PycharmProjects\homework\PA3\scoreboard\scoreboard-10.png', ]],
    'end': [r'C:\Users\zhang\PycharmProjects\homework\PA3\ending\game-over.png',
            r'C:\Users\zhang\PycharmProjects\homework\PA3\ending\restart-1.png',
            r'C:\Users\zhang\PycharmProjects\homework\PA3\ending\restart-2.png',
            r'C:\Users\zhang\PycharmProjects\homework\PA3\ending\restart-3.png',
            r'C:\Users\zhang\PycharmProjects\homework\PA3\ending\restart-4.png',
            r'C:\Users\zhang\PycharmProjects\homework\PA3\ending\restart-5.png',
            r'C:\Users\zhang\PycharmProjects\homework\PA3\ending\restart-6.png',
            r'C:\Users\zhang\PycharmProjects\homework\PA3\ending\restart-7.png',
            r'C:\Users\zhang\PycharmProjects\homework\PA3\ending\restart-8.png', ]

}
AUDIO_PATHS = {'dinosaur': [r'C:\Users\zhang\PycharmProjects\homework\PA3\jump.mp3',
                            r'C:\Users\zhang\PycharmProjects\homework\PA3\die.mp3',
                            r'C:\Users\zhang\PycharmProjects\homework\PA3\score.mp3']}

game_status = 'start'
mode = 'day'
screen_color_rate = 0
screen_color = (255, 255, 255)
