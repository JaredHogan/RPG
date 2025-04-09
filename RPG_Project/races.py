from abc import ABC
import pygame as pg

'This will contain all the different races that can be used'
'for the characters in the game'


class Race(ABC):
    # The character and the NPCs will have a race that defines their starting
    #  stats, and maybe a racial ability
    # @abstractmethod
    def racial_ability(self):
        pass


class Human(Race):
    # A class that focuses on nothing but is weak in nothing
    def __init__(self):
        self.name = "Human"

    def load_animations(self, anim):
        # use raw strings.
        base_path = fr"RPG_Project\images\Character without weapon\"
        directions = ['up', 'down', 'left', 'right']
        animations = {}
        for direction in directions:
            animation_frames = []
            for i in range(1, 5):
                # use raw strings.
                file_name = fr"\{anim}\{direction}\{anim} {direction}{i}.png"
                full_path = base_path + file_name
                try:
                    frame = pg.image.load(full_path).convert_alpha()
                    o_width = frame.get_width()
                    o_height = frame.get_height()
                    width = int(o_width * (256 / o_height))
                    scaled_image = pg.transform.scale(frame, (width, 256))
                    animation_frames.append(scaled_image)
                except pg.error as e:
                    print(f"Error loading image: {full_path}, {e}")
                    # Handle error, perhaps by appending a default image.
                    default_image = pg.Surface((64, 64))
                    default_image.fill((255, 0, 255))
                    animation_frames.append(default_image)

            animations[direction] = animation_frames
        return animations

    def racial_ability(self):
        print('Human Racial Ability')


class Orc(Race):
    # A race that focuses on large, two handed weapons going bonk
    def racial_ability(self):
        print('Orc Racial Ability')


class Elf(Race):
    # A race that will get extra mana to be able to cast more spells
    def racial_ability(self):
        print('Elf Racial Ability')


class Dwarf(Race):

    def racial_ability(self):
        pass
