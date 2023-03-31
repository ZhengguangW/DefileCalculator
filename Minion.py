class Minion:
    def __init__(self,attack,health,name,owner):
        self.attack=attack
        self.health=health
        self.name=name
        self.owner=owner

    def battle(self,anothercard):
        self.health-=anothercard.attack
        anothercard.health-=self.attack
        return self.name+ "attack: "+anothercard.name
        
    def reverse(self,anothercard):
        self.health+=anothercard.attack
        anothercard.health+=self.attack