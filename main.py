import random

class Character():
    def __init__(self, pseudo:str, level:int, hp:int, initiative:int, mana = 0) -> None:
        self.pseudo = pseudo
        self.level = level
        self.hp = hp
        self.initiative = initiative
        self.mana = mana

    def __str__(self) -> str:
        return (f"Type Normal => {self.pseudo} level {self.level} with {self.hp} health. Initiative {self.initiative}. Mana {self.mana}")

    def checkIfDead(player):
        if player.hp <= 0:
            print(f'{player.pseudo} is dead !!')
            return False
        else:
            return True

    def damage(self):
        damage = self.level
        return damage

    def attack(player1, player2):
        if int(player1.initiative) > int(player2.initiative) and player1.checkIfDead() and player2.checkIfDead():
            player2.hp = int(player2.hp) - int(player1.damage())
            print(f"-{player1.damage()} hp to {player2.pseudo} (Current Hp : {player2.hp})")
            if player2.hp <= 0:
                player2.checkIfDead()
                return
            else:
                player1.hp = int(player1.hp) - int(player2.damage())
                print(f"-{player2.damage()} hp to {player1.pseudo} (Current Hp : {player1.hp})")
                player1.checkIfDead()
        elif int(player1.initiative) < int(player2.initiative) and player2.checkIfDead() and player1.checkIfDead():
            player1.hp = int(player1.hp) - int(player2.damage())
            print(f"-{player2.damage()} hp to {player1.pseudo} (Current Hp : {player1.hp})")
            if player1.hp <= 0:
                player2.checkIfDead()
                return
            else:
                player2.hp = int(player2.hp) - int(player1.damage())
                print(f"-{player1.damage()} hp to {player2.pseudo} (Current Hp : {player2.hp})")
                player2.checkIfDead()
        elif int(player1.initiative) == int(player2.initiative):
            player1.hp = int(player1.hp) - int(player2.damage())
            print(f"-{player2.damage()} hp to {player1.pseudo} (Current Hp : {player1.hp})")
            player2.hp = int(player2.hp) - int(player1.level)
            print(f"-{player1.damage()} hp to {player2.pseudo} (Current Hp : {player2.hp})")
        return

    def fight(player1, player2):
        while int(player1.hp) > 0 and int(player2.hp) > 0:
            player1.attack(player2)

    def heal(self):
        soin = random.randint(1,self.level)
        if self.hp > 0:
            self.hp = self.hp + soin
            print(f"{self.pseudo} just healed himself. HP +{soin}")
        elif self.hp <= 0:
            print(f"{self.pseudo} is dead and can't heal")
        return


class Guerrier(Character):
    def __init__(self, pseudo:str, level:int) -> None:
        self.pseudo = pseudo
        self.level = level
        self.hp = level * 8 + 4
        self.initiative = level * 4 + 6
        super().__init__(self.pseudo, self.level, self.hp, self.initiative)

    def __str__(self) -> str:
        return (f"Type Guerrier => {self.pseudo} level {self.level} with {self.hp} health. Initiative {self.initiative}. Mana {self.mana}")

    def damage(self):
        damage = self.level * 2
        return damage


class Mage(Character):
    def __init__(self, pseudo:str, level:int) -> None:
        self.pseudo = pseudo
        self.level = level
        self.hp = level * 5 + 10
        self.initiative = level * 6 + 4
        self.mana = level * 5
        super().__init__(self.pseudo, self.level, self.hp, self.initiative, self.mana)


    def __str__(self) -> str:
        return (f"Type Mage => {self.pseudo} level {self.level} with {self.hp} health. Initiative {self.initiative}. Mana {self.mana}")

    def damage(self):
        if self.mana > 0:
            damage = self.level + 3
            self.mana = self.mana - 4
        else:
            damage = self.level
        return damage


class Player():
    def __init__(self, name:str, character:list) -> None:
        self.name = name
        self.character = character
        self.max_char = 3

    def __str__(self) -> str:
        alive = []
        dead = []
        for i in self.character:
            if i.hp > 0:
                alive.append(i)
            elif i.hp <= 0:
                dead.append(i)
        return (f"{self.name} has {len(self.character)} character. Alive : {len(alive)} Dead : {len(dead)}")
    
    def add_character(self, new_character):
        if len(self.character) >= self.max_char or new_character in self.character:
            print(f"{self.name} already have reached the max amount of character, or already have {new_character.pseudo}")
        elif len(self.character) < self.max_char and new_character not in self.character:
            self.character.append(new_character)
            print(f"{self.name} got a new character: {new_character}")
    
    def get_character1(self, number:int):
        char = self.character[number-1]
        print(f"{self.name} has => {char.__str__()}")
        return

    def get_character2(self, name):
        for i in self.character:
            if i.pseudo == name:
                print(f"{self.name} has => {i.__str__()}")
        return

    def get_character3(self, character):
        for i in self.character:
            if i == character:
                print(f"{self.name} has => {i.__str__()}")
        return

    def remove_character1(self, number:int):
        char = self.character[number-1]
        self.character.pop(number-1)
        print(f"{self.name} remove => {char.pseudo}")
        return

    def remove_character2(self, name):
        for i in self.character:
            if i.pseudo == name:
                index_i = self.character.index(i)
                self.character.pop(index_i)
                print(f"{self.name} remove => {i.pseudo}")
        return

    def remove_character3(self, character):
        for i in self.character:
            if i == character:
                index_i = self.character.index(i)
                self.character.pop(index_i)
                print(f"{self.name} remove => {i.pseudo}")
        return

    def challenge(self, player):
        p1_list = self.character
        p2_list = player.character
        for i in range(len(p1_list)+len(p2_list)):
            for p1 in range(len(p1_list)):
                if p1_list[p1].hp > 0:
                    p1_fight = p1_list[p1]
                elif p1_list[p1].hp <= 0:
                    p1_list.pop(p1)
            for p2 in range(len(p2_list)):
                if p2_list[p2].hp > 0:
                    p2_fight = p2_list[p2]
                elif p2_list[p2].hp <= 0:
                    p2_list.pop(p2)
            p1_fight.fight(p2_fight)
            if len(p1_list) == 0:
                print(f"{self.name} lost against {player.name}")
            elif len(p2_list) == 0:
                print(f"{player.name} lost against {self.name}")
        return
    

frodon = Character("Frodon",10, 100, 11)
smeagol = Character("Sméagol",12, 100, 10)
aragorn = Guerrier('Aragorn',100)
gandalf = Mage('Gandalf', 100)
radagast = Mage('Radagast', 110)
sarouman = Mage('Sarouman', 600)
enzo = Player('Enzo', [frodon,smeagol])
raphael = Player('Raphael', [gandalf,aragorn,radagast])
samuel = Player('Samuel', [sarouman])


samuel.challenge(enzo)