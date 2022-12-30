import random

class Personnage():
    def __init__(self, pseudo:str, niveau:int, pdv:int, initiative:int, mana = 0) -> None:
        self.pseudo = pseudo
        self.niveau = niveau
        self.pdv = pdv
        self.initiative = initiative
        self.mana = mana

    def __str__(self) -> str:
        return (f"{self.pseudo} niveau {self.niveau} avec {self.pdv} points de vie. Initiative {self.initiative}")

    def checkIfDead(player):
        if player.pdv <= 0:
            print(f'{player.pseudo} is dead !!')
            return False
        else:
            return True

    def attaquer(player1, player2):
        if int(player1.initiative) > int(player2.initiative) and player1.checkIfDead() and player2.checkIfDead():
            player2.pdv = int(player2.pdv) - int(player1.niveau)
            print(f"-{player1.niveau} hp to {player2.pseudo} (Current Hp : {player2.pdv})")
            if player2.pdv <= 0:
                return
            else:
                player1.pdv = int(player1.pdv) - int(player2.niveau)
                print(f"-{player2.niveau} hp to {player1.pseudo} (Current Hp : {player1.pdv})")
                player1.checkIfDead()
        elif int(player1.initiative) < int(player2.initiative) and player2.checkIfDead() and player1.checkIfDead():
            player1.pdv = int(player1.pdv) - int(player2.niveau)
            print(f"-{player2.niveau} hp to {player1.pseudo} (Current Hp : {player1.pdv})")
            if player1.pdv <= 0:
                return
            else:
                player2.pdv = int(player2.pdv) - int(player1.niveau)
                print(f"-{player1.niveau} hp to {player2.pseudo} (Current Hp : {player2.pdv})")
                player2.checkIfDead()
        elif int(player1.initiative) == int(player2.initiative):
            player1.pdv = int(player1.pdv) - int(player2.niveau)
            print(f"-{player2.niveau} hp to {player1.pseudo} (Current Hp : {player1.pdv})")
            player2.pdv = int(player2.pdv) - int(player1.niveau)
            print(f"-{player1.niveau} hp to {player2.pseudo} (Current Hp : {player2.pdv})")
        return

    def combat(player1, player2):
        while int(player1.pdv) > 0 and int(player2.pdv) > 0:
            player1.attaquer(player2)

    def soigner(self):
        soin = random.randint(1,self.niveau)
        if self.pdv > 0:
            self.pdv = self.pdv + soin
            print(f"{self.pseudo} just healed himself. HP +{soin}")
        elif self.pdv <= 0:
            print(f"{self.pseudo} is dead and can't heal")
        return



class Guerrier(Personnage):
    def __init__(self, pseudo:str, niveau:int, pdv:int, initiative:int) -> None:
        super().__init__(pseudo, niveau, pdv, initiative)
        self.pseudo = str(pseudo)
        self.niveau = int(niveau)
        self.pdv = int(niveau) * 8 + 4
        self.initiative = int(niveau) * 4 + 6

    def __str__(self) -> str:
        return (f"Type Guerrier => {self.pseudo} niveau {self.niveau} avec {self.pdv} points de vie. Initiative {self.initiative}")

    def checkIfDead(player):
        if player.pdv <= 0:
            print(f'{player.pseudo} is dead !!')
            return False
        else:
            return True

    def attaquer(player1, player2):
        if int(player1.initiative) > int(player2.initiative) and player1.checkIfDead() and player2.checkIfDead():
            player2.pdv = int(player2.pdv) - int(player1.niveau)
            print(f"-{player1.niveau} hp to {player2.pseudo} (Current Hp : {player2.pdv})")
            if player2.pdv <= 0:
                return
            else:
                player1.pdv = int(player1.pdv) - int(player2.niveau)
                print(f"-{player2.niveau} hp to {player1.pseudo} (Current Hp : {player1.pdv})")
                player1.checkIfDead()
        elif int(player1.initiative) < int(player2.initiative) and player2.checkIfDead() and player1.checkIfDead():
            player1.pdv = int(player1.pdv) - int(player2.niveau)
            print(f"-{player2.niveau} hp to {player1.pseudo} (Current Hp : {player1.pdv})")
            if player1.pdv <= 0:
                return
            else:
                player2.pdv = int(player2.pdv) - int(player1.niveau)
                print(f"-{player1.niveau} hp to {player2.pseudo} (Current Hp : {player2.pdv})")
                player2.checkIfDead()
        elif int(player1.initiative) == int(player2.initiative):
            player1.pdv = int(player1.pdv) - int(player2.niveau)
            print(f"-{player2.niveau} hp to {player1.pseudo} (Current Hp : {player1.pdv})")
            player2.pdv = int(player2.pdv) - int(player1.niveau)
            print(f"-{player1.niveau} hp to {player2.pseudo} (Current Hp : {player2.pdv})")
        return

    def combat(player1, player2):
        while int(player1.pdv) > 0 and int(player2.pdv) > 0:
            player1.attaquer(player2)

    def soigner(self):
        soin = random.randint(1,self.niveau)
        if self.pdv > 0:
            self.pdv = self.pdv + soin
            print(f"{self.pseudo} just healed himself. HP +{soin}")
        elif self.pdv <= 0:
            print(f"{self.pseudo} is dead and can't heal")
        return

class Mage(Personnage):
    def __init__(self, pseudo:str, niveau:int, pdv:int, initiative:int, mana:int) -> None:
        super().__init__(pseudo, niveau, pdv, initiative, mana)
        self.pseudo = str(pseudo)
        self.niveau = int(niveau)
        self.pdv = int(niveau) * 5 + 10
        self.initiative = int(niveau) * 6 + 4
        self.mana = int(niveau) * 5

    def __str__(self) -> str:
        return (f"Type Mage => {self.pseudo} niveau {self.niveau} avec {self.pdv} points de vie. Initiative {self.initiative}")

    def checkIfDead(player):
        if player.pdv <= 0:
            print(f'{player.pseudo} is dead !!')
            return False
        else:
            return True

    def attaquer(player1, player2):
        if int(player1.initiative) > int(player2.initiative) and player1.checkIfDead() and player2.checkIfDead():
            player2.pdv = int(player2.pdv) - int(player1.niveau)
            print(f"-{player1.niveau} hp to {player2.pseudo} (Current Hp : {player2.pdv})")
            if player2.pdv <= 0:
                return
            else:
                player1.pdv = int(player1.pdv) - int(player2.niveau)
                print(f"-{player2.niveau} hp to {player1.pseudo} (Current Hp : {player1.pdv})")
                player1.checkIfDead()
        elif int(player1.initiative) < int(player2.initiative) and player2.checkIfDead() and player1.checkIfDead():
            player1.pdv = int(player1.pdv) - int(player2.niveau)
            print(f"-{player2.niveau} hp to {player1.pseudo} (Current Hp : {player1.pdv})")
            if player1.pdv <= 0:
                return
            else:
                player2.pdv = int(player2.pdv) - int(player1.niveau)
                print(f"-{player1.niveau} hp to {player2.pseudo} (Current Hp : {player2.pdv})")
                player2.checkIfDead()
        elif int(player1.initiative) == int(player2.initiative):
            player1.pdv = int(player1.pdv) - int(player2.niveau)
            print(f"-{player2.niveau} hp to {player1.pseudo} (Current Hp : {player1.pdv})")
            player2.pdv = int(player2.pdv) - int(player1.niveau)
            print(f"-{player1.niveau} hp to {player2.pseudo} (Current Hp : {player2.pdv})")
        return

    def combat(player1, player2):
        while int(player1.pdv) > 0 and int(player2.pdv) > 0:
            player1.attaquer(player2)

    def soigner(self):
        soin = random.randint(1,self.niveau)
        if self.pdv > 0:
            self.pdv = self.pdv + soin
            print(f"{self.pseudo} just healed himself. HP +{soin}")
        elif self.pdv <= 0:
            print(f"{self.pseudo} is dead and can't heal")
        return


kevinou = Personnage("Kevan",10, 100, 11)
raphou = Personnage("Raphael",12, 100, 10)
enzo = Guerrier('Enzo',100, 100, 12)
elea = Mage('Elea', 100, 50, 16, 100)
anaita = Mage('Anaita', 110, 60, 14, 80)


enzo.combat(anaita)