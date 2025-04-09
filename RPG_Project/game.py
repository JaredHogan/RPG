'This is the main file of my RPG final project'
import pygame as pg
import characters
import races
import jobs
import sprites
import math

# General setup


WINDOW_WIDTH, WINDOW_HEIGHT = (2560/2, 1440/2)
display_surface = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pg.display.set_caption('RPG')
pg.init()
display_surface.fill('black')


def main_menu(display_surface: pg.surface):
    pass


def overworld():
    global display_surface
    WINDOW_WIDTH, WINDOW_HEIGHT = (2560/2, 1440/2)
    clock = pg.time.Clock()
    dt = clock.tick(120) / 1000
    running = True
    frame_counter = 0
    all_sprites = pg.sprite.Group()
    enemy_sprites = pg.sprite.Group()
    buttons = pg.sprite.Group()
    player = characters.Player('Jared')
    player.sprite = sprites.Player_OW(all_sprites)
    all_sprites.draw(display_surface)

    while running:
        display_surface.fill('darkgrey')
        pos = pg.mouse.get_pos()
        keys = pg.key.get_pressed()
        events = pg.event.get()
        if keys[pg.K_ESCAPE]:
            running = False
        for ev in events:
            if ev.type == pg.QUIT:
                running = False
                break
        frame_counter += 1
        pg.display.update()
        all_sprites.update(dt)
        clock.tick(120)

    pg.quit()


overworld()
