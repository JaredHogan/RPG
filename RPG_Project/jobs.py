'This will have all of the jobs available for the characters in the game'
from abc import ABC
import actions


class Job(ABC):
    # The character and most NPCs will have a job/class of some kind that
    # defines their available actions
    pass


class Warrior(Job):
    # Job that focuses on hitting hard with melee weapons, disregarding magic
    def __init__(self):
        self.job_name = 'Warrior'

    S_STATS = {
        'Vigor': [15, 5],
        'Endurence': [15, 3],
        'Mind': [8, 0],
        'Strength': [15, 5],
        'Focus': [8, 0],
        'Divinity': [8, 0],
        'Unallocated': [0, 3]
    }

    S_ACTIONS = {
        'Punch': actions.Punch(),
        'Longsword': actions.Longsword()
    }


class SpellSword(Job):
    # Job that has some magic and some melee
    def __init__(self):
        self.job_name = 'SpellSword'

    S_STATS = {
        'Vigor': [13, 3],
        'Endurence': [13, 3],
        'Mind': [10, 0],
        'Strength': [15, 5],
        'Focus': [10, 0],
        'Divinity': [8, 0],
        'Unallocated': [0, 3]
    }


class Monk(Job):
    # Job that has some divinity and some melee
    def __init__(self):
        self.job_name = "Monk"

    S_STATS = {
        'Vigor': [13, 3],
        'Endurence': [13, 3],
        'Mind': [10, 0],
        'Strength': [15, 5],
        'Focus': [8, 0],
        'Divinity': [10, 0],
        'Unallocated': [0, 3]
    }


class Wizard(Job):
    # Job that focuses on channels and big damage
    def __init__(self):
        self.job_name = 'Wizard'

    S_STATS = {
        'Vigor': [8, 2],
        'Endurence': [10, 1],
        'Mind': [10, 4],
        'Strength': [10, 1],
        'Focus': [15, 5],
        'Divinity': [15, 2],
        'Unallocated': [0, 3]
    }


class Sorcerer(Job):
    # Job that focuses on faster, smaller damage
    def __init__(self):
        self.job_name = 'Sorcerer'

    S_STATS = {
        'Vigor': [8, 2],
        'Endurence': [10, 1],
        'Mind': [10, 4],
        'Strength': [10, 1],
        'Focus': [15, 5],
        'Divinity': [15, 2],
        'Unallocated': [0, 3]
    }

    S_ACTIONS = {
        'Fireball': actions.Fireball(),
        'Lightning': actions.Lightning()
    }


class Priest(Job):
    # Job that focuses on support magic
    def __init__(self):
        self.job_name = 'Priest'

    S_STATS = {
        'Vigor': [8, 2],
        'Endurence': [10, 1],
        'Mind': [10, 4],
        'Strength': [10, 1],
        'Focus': [15, 2],
        'Divinity': [15, 5],
        'Unallocated': [0, 3]
    }


class Witch(Job):
    # Job that focuses on debuff magic
    def __init__(self):
        self.job_name = 'Witch'

    S_STATS = {
        'Vigor': [8, 2],
        'Endurence': [10, 1],
        'Mind': [10, 4],
        'Strength': [10, 1],
        'Focus': [15, 2],
        'Divinity': [15, 5],
        'Unallocated': [0, 3]
    }
