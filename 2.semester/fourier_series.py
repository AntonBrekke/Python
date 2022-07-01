import pygame as pg
import numpy as np
import os

os.environ['SDL_VIDEO_CENTERED'] = '1'

# pygame konfigurasjoner
width, height = 1920, 1080

fps = 30
pg.display.set_caption("Fourier Tranform")
screen = pg.display.set_mode((width, height))
clock = pg.time.Clock()

# Farger
white = (255, 255, 255)
gray = (150, 150, 150)
black = (0, 0, 0)
crimson = (230, 20, 32)
blue = (0, 153, 153)

N = 1
time = 0
radius = 0
pos_x = 600
pos_y = 520
wave_list = []
offset = 600

Iterations = 5

run = True
while run:
    clock.tick(fps)
    screen.fill(black)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    x = pos_x
    y = pos_y
    for i in range(Iterations):
        old_x, old_y = x, y

        N = i*2 + 1      # Oddetall
        radius = 150*(4/(N * np.pi))
        x += int(radius*np.cos(N*time))
        y += int(radius * np.sin(N*time))

        pg.draw.circle(screen, blue, (old_x, old_y), int(radius), 2)
        pg.draw.line(screen, white, (old_x, old_y), (x,y), 3)
        pg.draw.circle(screen, crimson, (x,y), 5)
    wave_list.insert(0, y)
    if len(wave_list) > 1000:
        wave_list.pop()

    pg.draw.line(screen, white, (x, y), (pos_x + offset, wave_list[0]), 3)

    for index in range(len(wave_list)):
        pg.draw.circle(screen, white, (index + pos_x + offset, wave_list[index]), 2)
    time += 0.01
    pg.display.update()

pg.quit()
