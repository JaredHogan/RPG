import pygame as pg
from os.path import join
from abc import ABC
import races


class Player_OW(pg.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        display_info = pg.display.Info()
        WINDOW_WIDTH, WINDOW_HEIGHT = display_info.current_w, display_info.current_h
        self.race = races.Human()
        self.walk = self.race.load_animations('walk')
        self.idle = self.race.load_animations('idle')
        self.animation = self.idle
        self.facing = 'down'
        self.image = self.animation[self.facing][0]
        self.rect = self.image.get_frect(
            center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        self.frame_counter = 0
        self.frame = 0
        self.animation_speed = 10
        self.speed = 300
        self.direction = pg.Vector2()

    def set_vector(self, dt):
        keys = pg.key.get_pressed()
        self.direction.x = int(keys[pg.K_d]) - int(keys[pg.K_a])
        self.direction.y = int(keys[pg.K_s]) - int(keys[pg.K_w])
        self.vector = self.direction.normalize() * self.speed * \
            dt if self.direction else self.direction

    def set_facing(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.facing = 'up'

        if keys[pg.K_s]:
            self.facing = 'down'

        if keys[pg.K_a]:
            self.facing = 'left'

        if keys[pg.K_d]:
            self.facing = 'right'

    def set_animation(self):
        if self.vector.magnitude() != 0:
            self.animation = self.walk
            self.animation_speed = 10
        else:
            self.animation = self.idle
            self.animation_speed = 20

    def set_frame(self):
        if self.frame_counter >= self.animation_speed:
            self.frame_counter = 0
            self.frame = (self.frame + 1) % 4
            self.image = self.animation[self.facing][self.frame]
        else:
            self.image = self.animation[self.facing][self.frame]

    def update(self, dt):
        self.set_vector(dt)
        self.set_facing()
        self.set_animation()
        self.set_frame()
        self.frame_counter += 1
        self.rect.center += self.vector * self.speed * dt


class Enemy(pg.sprite.Sprite):
    def __init__(self, name: str, lvl: int, *groups):
        super().__init__(*groups)
        self.name = name
        self.race = races.Human()
        self.animation = self.race.load_animations('idle')
        self.facing = 'down'
        self.animation_speed = 20
        self.frame = 0
        self.frame_counter = 0
        self.image = self.animation[self.facing][0]
        self.rect = self.image.get_frect(
            center=(300, 300))

    def set_frame(self):
        if self.frame_counter >= self.animation_speed:
            self.frame_counter = 0
            self.frame = (self.frame + 1) % 4
            self.image = self.animation[self.facing][self.frame]

    def update(self, dt):
        self.set_frame()
        self.frame_counter += 1


class button(pg.sprite.Sprite):
    def __init__(self, text, font: pg.Font, *groups):
        super().__init__(*groups)
        display_info = pg.display.Info()
        WINDOW_WIDTH, WINDOW_HEIGHT = display_info.current_w, display_info.current_h

        # Render the text surfaces
        self.normal_text = font.render(text, True, 'black')
        self.hovered_text = font.render(text, True, 'darkgrey')
        self.pressed_text = font.render(text, True, 'lightblue')

        # Create background surfaces
        self.normal_image = pg.Surface(self.normal_text.get_size())
        self.normal_image.fill('red')  # Set background color to red
        # Blit text onto background.
        self.normal_image.blit(self.normal_text, (0, 0))

        self.hovered_image = pg.Surface(self.hovered_text.get_size())
        self.hovered_image.fill('red')
        self.hovered_image.blit(self.hovered_text, (0, 0))

        self.pressed_image = pg.Surface(self.pressed_text.get_size())
        self.pressed_image.fill('red')
        self.pressed_image.blit(self.pressed_text, (0, 0))

        self.image = self.normal_image
        self.rect = self.image.get_frect(
            center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

        self.pressed = False
        self.pressed_cd_until = pg.time.get_ticks() + 2000

    def update(self, dt):
        pos = pg.mouse.get_pos()
        lmb = pg.mouse.get_pressed()[0]
        time = pg.time.get_ticks()

        if not self.pressed:
            self.image = self.normal_image
            if self.rect.collidepoint(pos):
                self.image = self.hovered_image
                if lmb and time >= self.pressed_cd_until:
                    self.pressed_cd_until = pg.time.get_ticks() + 2000
                    self.pressed = True
                    self.image = self.pressed_image
        if self.pressed:
            if time >= self.pressed_cd_until:
                self.pressed = False
