class Minion:
    def __init__(self,attack,health,name,owner):
        self.attack=attack
        self.health=health
        self.name=name
        self.owner=owner

        self.attack_time=1

    def battle(self,anothercard):
        self.health-=anothercard.attack
        anothercard.health-=self.attack
        self.attack_time-=1
        return self.name+ "attack: "+anothercard.name
        
    def reverse(self,anothercard):
        self.health+=anothercard.attack
        anothercard.health+=self.attack
        self.attack_time+=1

    def left_attacktime(self):
        if self.attack_time>=1:
            return True
        else:
            return False