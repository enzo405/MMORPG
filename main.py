import random

class Personnage():
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


class Guerrier(Personnage):
    def __init__(self, pseudo:str, level:int, hp:int, initiative:int) -> None:
        super().__init__(pseudo, level, hp, initiative)
        self.pseudo = str(pseudo)
        self.level = int(level)
        self.hp = int(level) * 8 + 4
        self.initiative = int(level) * 4 + 6

    def __str__(self) -> str:
        return (f"Type Guerrier => {self.pseudo} level {self.level} with {self.hp} health. Initiative {self.initiative}. Mana {self.mana}")

    def damage(self):
        damage = self.level * 2
        return damage


class Mage(Personnage):
    def __init__(self, pseudo:str, level:int, hp:int, initiative:int, mana:int) -> None:
        super().__init__(pseudo, level, hp, initiative, mana)
        self.pseudo = str(pseudo)
        self.level = int(level)
        self.hp = int(level) * 5 + 10
        self.initiative = int(level) * 6 + 4
        self.mana = int(level) * 5

    def __str__(self) -> str:
        return (f"Type Mage => {self.pseudo} level {self.level} with {self.hp} health. Initiative {self.initiative}. Mana {self.mana}")

    def damage(self):
        if self.mana > 0:
            damage = self.level + 3
            self.mana = self.mana - 4
        else:
            damage = self.level
        return damage


kevinou = Personnage("Kevan",10, 100, 11)
raphou = Personnage("Raphael",12, 100, 10)
enzo = Guerrier('Enzo',100, 100, 12)
elea = Mage('Elea', 100, 50, 16, 100)
anaita = Mage('Anaita', 110, 60, 14, 80)


enzo.fight(anaita)
elea.fight(anaita)
elea.fight(kevinou)