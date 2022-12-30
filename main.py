import random

class Personnage():
    def __init__(self, pseudo:str, niveau:int, pdv:int, initiative:int) -> None:
        self.pseudo = str(pseudo)
        self.niveau = int(niveau)
        self.pdv = int(pdv)
        self.initiative = int(initiative)

    def __str__(self) -> str:
        return (f"{self.pseudo} niveau {self.niveau} avec {self.pdv} points de vie. Initiative {self.initiative}")

    def checkIfDead(player):
        if player.pdv <= 0:
            print(f'{player.pseudo} est mort !!')
        return

    def attaquer(player1, player2):
        if int(player1.initiative) > int(player2.initiative):
            player2.pdv = int(player2.pdv) - int(player1.niveau)
            print(f"{player1.pseudo} vient d'enlever {player1.niveau} pdv à {player2.pseudo}")
            if player2.pdv <= 0:
                player2.checkIfDead()
                return
            else:
                player1.pdv = int(player1.pdv) - int(player2.niveau)
                print(f"{player2.pseudo} vient d'enlever {player2.niveau} pdv à {player1.pseudo}")
            player1.checkIfDead()
        elif int(player1.initiative) < int(player2.initiative):
            player1.pdv = int(player1.pdv) - int(player2.niveau)
            print(f"{player2.pseudo} vient d'enlever {player2.niveau} pdv à {player1.pseudo}")
            if player1.pdv <= 0:
                player1.checkIfDead()
                return
            else:
                player2.pdv = int(player2.pdv) - int(player1.niveau)
                print(f"{player1.pseudo} vient d'enlever {player1.niveau} pdv à {player2.pseudo}")
            player2.checkIfDead()
        elif int(player1.initiative) == int(player2.initiative):
            player1.pdv = int(player1.pdv) - int(player2.niveau)
            print(f"{player2.pseudo} vient d'enlever {player2.niveau} pdv à {player1.pseudo}")
            player2.pdv = int(player2.pdv) - int(player1.niveau)
            print(f"{player1.pseudo} vient d'enlever {player1.niveau} pdv à {player2.pseudo}")
            player1.checkIfDead()
            player2.checkIfDead()
        return

    def combat(player1, player2):
        while int(player1.pdv) > 0 and int(player2.pdv) > 0:
            player1.attaquer(player2)
        print(player1)
        print(player2)

    def soigner(self):
        soin = random.randint(1,self.niveau)
        self.pdv = self.pdv + soin
        print(f"{self.pseudo} vient de se soigner de {soin} pdv")
        return

kevinou = Personnage("Kevan","10", "100", "11")
raphou = Personnage("Raphael","12", "100", "10")

raphou.attaquer(kevinou)
kevinou.soigner()
kevinou.combat(raphou)
