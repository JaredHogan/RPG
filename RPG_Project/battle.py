import characters


class Battle(characters.Party):
    def __init__(self, friendly_party: characters.Party,
                 enemy_party: characters.Party):
        self.party = friendly_party
        self.enemies = enemy_party
        self.turn_count = 1
        self.fighting = True

    def check_win(self):
        return True if len(self.enemies.members) == 0 else False

    def check_lose(self):
        return True if len(self.party) == 0 else False

    def check_end(self):
        if self.check_lose() is True:
            print("You lose!")
            return True
        if self.check_win() is True:
            print("You win!")
            return True
        else:
            return False
    gone = []
    while self.fighting is True:
        gone = []
        while len(gone) != len(self.friendlymembers()) and fighting is True:
            i = 1
            if len(gone) == 0:
                print("Which member will go first?")
            else:
                print("Who's next?")

            for member in self.members:
                if member.name in gone:
                    print(f"{i}: {member.name} (exhausted)")
                else:
                    print(f"{i}: {member.name}")
                i += 1
            print(f"{i}: Run")
            choice = int(input())
            if choice == i:
                print("You run.")
                fighting = False
                continue
            user = self.members[choice-1]
            if user.name in gone:
                print("Please pick someone who can still move.")
                time.sleep(1)
                continue
            i = 1
            print(f"{user.name} : {user.pools}")
            for action in self.members[choice-1].get_actions():
                print(f"{i}: {action}")
                i += 1
            print(f"{i}: Pass")
            move = int(input())
            if move == i:
                gone.append(user.name)
                continue
            action = self.members[choice-1].get_actions()[move-1]
            print("Targeting who?")
            i = 1
            for member in enemy_party.members:
                print(f"{i}: {member.name} : {member.pools}")

            target_key = int(input())-1
            target = enemy_party.members[target_key]
            action.activate(user, target)

            print(f"{target.name}: {target.pools}")
            self.remove_dead()
            enemy_party.remove_dead()
            fighting = not check_end(self.members, enemy_party.members)
            gone.append(user.name)
        if fighting:
            i = 0
            for member in enemy_party.members:
                move = list(member.actions.keys())[random.randint(
                    0, len(member.get_actions())-1)]
                target = self.members[random.randint(
                    0, len(self.members)-1)]
                print(f"{member.name} uses {move} against {target.name}")
                member.actions[move].activate(member, target)
                time.sleep(1)
                print(f'{target.name}: {target.pools}')
                time.sleep(1)
                self.remove_dead()
                enemy_party.remove_dead()
                fighting = not check_end(self.members, enemy_party.members)
            turn_count += 1
