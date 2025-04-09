import pygame as pg
from os.path import join
import races


class Player_OW(pg.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(groups)
        self.race = races.Human()
        self.walk = self.race.load_animations('walk')
        self.idle = self.race.load_animations('idle')
        self.animation = self.idle
        self.facing = 'down'
        self.image = self.animation[self.facing][0]
        self.rect = self.image.get_frect(center=(300, 300))
        self.frame_counter = 0
        self.frame = 0
        self.animation_speed = 10
        self.speed = 300
        self.direction = pg.Vector2()

    def set_vector(self, keys, dt):
        self.direction.x = int(keys[pg.K_d]) - int(keys[pg.K_a])
        self.direction.y = int(keys[pg.K_s]) - int(keys[pg.K_w])
        self.vector = self.direction.normalize() * self.speed * \
            dt if self.direction else self.direction

    def set_facing(self, keys):
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
        keys = pg.key.get_pressed()
        self.set_vector(keys, dt)
        self.set_facing(keys)
        self.set_animation()
        self.set_frame()
        self.frame_counter += 1
        self.rect.center += self.vector * self.speed * dt


class Enemy(pg.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
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


class Button(pg.sprite.Sprite):
    pass
