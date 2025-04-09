from tabulate import tabulate
import actions
import races
import jobs
import random
import time


class Character(races.Race, jobs.Job):
    # every being in the game will be a character of some sort,
    def __init__(self, name='', lvl=1,
                 race=races.Human(), job=jobs.Warrior()):
        super().__init__()
        self.sprite = None
        self.name = name
        self.lvl = lvl
        self.race = race
        self.job = job
        self.stats = self.job.S_STATS
        self.actions = self.job.S_ACTIONS
        self.pools = [0, 0, 0]
        self.full_restore()
        self.conditions = []

    def full_restore(self):
        i = 0
        for stat in self.get_stats('V', 'E', 'M'):
            self.pools[i] = 10*stat
            i += 1

    def get_stats(self, *args):
        stats = []
        if 1 <= len(args) <= 6:
            for letter in args:
                i = 0
                for value in self.stats:
                    if value[0] == letter:
                        stats.append(self.stats[value][0])
                    i += 1
            if len(stats) == 1:
                stats = stats[0]
            return stats
        
    # def lvlup(self):
    #     newstats = []
    #     for stat in self.get_stats().values():
    #         newstats = 

        elif len(args) == 0:
            print('Received request for all stats')
            for stat_name, (stat, boost) in self.stats.items():
                stats.append([stat_name, stat])
            return stats

        else:
            print('Received request for more stats than 6')

    def get_actions(self):
        return list(self.actions.values())

    # ^^^write a action list getter so players
    # can see what options they have^^^

    def read_stats(self):
        stats = []
        stats.append([self.name, self.lvl])
        # stats.append('')
        for pair in self.get_stats():
            stats.append(pair)
        print(tabulate(stats, headers='firstrow', tablefmt="fsql"))

    def get_name(self):
        # name getter
        return self.name

    def get_lvl(self):
        # lvl getter
        return self.lvl

    def attack(self):
        # attack: Opens the attack list for the character.
        # Have a default for monsters? Maybe a random list or some logic?
        pass

    def lvlup(self):
        # applies stat boosts based on job to own stats
        for stat_name, stat, boost in self.stats:
            stat += boost
            print(f"{stat_name} increased to {stat}!")


class Player(Character):
    # Kinda important
    def __init__(self, name="Grebthar", lvl=1,
                 race=races.Human(), job=jobs.Warrior()):
        super().__init__(name, lvl, race, job)

        self.pos = (500, 500)

    def action(self):
        i = 1
        print("What would you like to do?\n")
        for action in self.actions:
            print(f"{i}: {action.name}")
            i += 1
        choice = int(input())
        choice -= 1
        print(self.actions)

    def get_anim(self, anim, frame) -> str:
        return self.animations[anim][frame-1]


def create_player() -> Player:
    name = input("What is your name?\n")\

    choice = input("what race are you?\n").lower()
    match choice:
        case 'human':
            race = races.Human()

        case 'orc':
            race = races.Orc()

        case 'elf':
            race = races.Elf()

    choice = input("What job are you?\n").lower()

    match choice:
        case 'warrior':
            job = jobs.Warrior()

        case 'spellsword':
            job = jobs.SpellSword()

        case 'monk':
            job = jobs.Monk()

        case 'wizard':
            job = jobs.Wizard()

        case 'sorcerer':
            job = jobs.Sorcerer()

        case 'priest':
            job = jobs.Priest()

        case 'witch':
            job = jobs.Witch()

    return Player(name, 1, race, job)


class Enemy(Character):

    def __init__(self, name='', lvl=1, race=races.Orc, job=jobs.Warrior):
        super().__init__(name, lvl, race, job)


class Party():
    def __init__(self):
        self.members: list[Character] = []

    def __str__(self):
        party = ''
        for member in self.members:
            party += f'\n{member.name}'
        return party

    def get_members(self):
        members = []
        for member in self.members:
            members.append(member)
        return members

    def remove_dead(self):
        self.members = [
            member for member in self.members if member.pools[0] > 0]

    
