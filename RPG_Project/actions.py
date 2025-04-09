from abc import ABC, abstractmethod
import math


class Action(ABC):
    def __str__(self):
        return self.name

    @abstractmethod
    def activate(self):
        pass


class Punch(Action):
    def __init__(self):
        self.name = 'Punch'
        self.cost = 3

    def activate(self, user, target):
        scaling = int(user.get_stats('S')*1)
        target.pools[0] = target.pools[0] - (5 + scaling)
        user.pools[1] = user.pools[1] - self.cost
        print('Punch!')


class Kick(Action):
    def __init__(self):
        self.name = 'Kick'

    def activate(self):
        print('Kick!')


class Longsword(Action):
    def __init__(self):
        self.name = 'Longsword'
        self.scaling = 2
        self.cost = 15
        self.legal_targets = [
            'Enemies'
        ]

    def activate(self, user, target):
        damage = (self.scaling * user.get_stats("S") + 10)
        target.pools[0] = target.pools[0] - damage
        user.pools[1] = user.pools[1] - self.cost
        print('Swish!')
        print(f"{damage} damage!")


class Fireball(Action):
    def __init__(self):
        self.name = "Firebolt"
        self.cost = 25
        self.scaling = 1
        self.legal_targets = [
            'Enemies'
        ]

    def activate(self, user, target):
        damage = (self.scaling * user.get_stats("F") + 15)
        target.pools[0] = target.pools[0] - damage
        user.pools[2] = user.pools[2] - self.cost
        print("Boom!")
        print(f"{damage} damage!")


class Lightning(Action):
    def __init__(self):
        self.name = 'Lightning (Channel)'
        self.cost = 40
        self.scaling = 3
        self.legal_targets = []

    def activate(self, user, target=None):
        if self.name == 'Lightning (Channel)':
            user.pools[2] = user.pools[2] - self.cost
            user.channeling = ['Lightning', user, target]
            self.name = 'Lightning'
            self.legal_targets.append('Enemies')
            print("Starting Lightning Channel")
        elif self.name == 'Lightning':
            damage = (self.scaling * user.get_stats("F") + 25)
            target.pools[0] = target.pools[0] - damage
            self.name = 'Lightning (Channel)'
            self.legal_targets.remove("Enemies")
            print("Kablam!")
            print(f"{damage} damage!")
