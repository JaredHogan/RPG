import pygame as pg
import math
import characters
import jobs
import races
import sprites

# General setup


def start_game():
    WINDOW_WIDTH, WINDOW_HEIGHT = (2560/2, 1440/2)
    display_surface = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pg.display.set_caption('RPG')
    pg.init()
    display_surface.fill('black')
    return display_surface

def main_menu(display_surface: pg.surface):
    pass


def overworld(display_surface: pg.surface):
    WINDOW_WIDTH, WINDOW_HEIGHT = (2560/2, 1440/2)
    clock = pg.time.Clock()
    dt = clock.tick(120) / 1000
    running = True
    frame_counter = 0
    display_surface = display_surface
    all_sprites = pg.sprite.Group()
    enemy_sprites = pg.sprite.Group()
    buttons = pg.sprite.Group()
    player = sprites.Player_OW(WINDOW_WIDTH, WINDOW_HEIGHT, all_sprites)
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
        clock.tick(120)

    pg.quit()
