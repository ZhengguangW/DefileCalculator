from Owner_enum import owner
class Minion:
    def __init__(self,attack,health,name,owner,divine_shield=False):
        self.attack=attack
        self.health=health
        self.name=name
        self.owner=owner
        self.attack_time=1
        self.divine_shield=divine_shield
        self.ds_status=False

    def battle(self,anothercard):
        if self.has_divine_shield() and anothercard.has_divine_shield():
            self.divine_shield=False
            self.ds_status=True
            anothercard.divine_shield=False
            anothercard.ds_status=True
        elif self.has_divine_shield():
            self.ds_status=True
            self.divine_shield=False
            anothercard.ds_status=False
            anothercard.health-=self.attack
        elif anothercard.has_divine_shield():
            anothercard.ds_status=True
            anothercard.divine_shield=False
            self.ds_status=False
            self.health-=anothercard.attack
        else:
            self.health-=anothercard.attack
            anothercard.health-=self.attack
            anothercard.ds_status=False
            self.ds_status=False
        self.attack_time-=1
        return self.name+ "attack: "+anothercard.name
        
    def reverse(self,anothercard):
        if self.ds_status and anothercard.ds_status:
            self.divine_shield=True
            self.ds_status=False
            anothercard.divine_shield=True
            anothercard.ds_status=False
        elif self.ds_status:
            self.divine_shield=True
            self.ds_status=False
            anothercard.health+=self.attack
        elif anothercard.ds_status:
            anothercard.divine_shield=True
            anothercard.ds_status=False
            self.health+=anothercard.attack
        else:
            self.health+=anothercard.attack
            anothercard.health+=self.attack
        self.attack_time+=1


    def left_attacktime(self):
        if self.attack_time>=1:
            return True
        else:
            return False
        

    def has_divine_shield(self):
        if self.divine_shield:
            return True
        else:
            return False
