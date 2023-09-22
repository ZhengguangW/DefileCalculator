from BackDefile.Owner_enum import owner
class Minion:
    def __init__(self,attack,health,name,owner,taunt,divine_shield,reborn):
        self.attack=attack
        self.health=health
        self.name=name
        self.owner=owner
        self.attack_time=1
        self.taunt=taunt
        self.divine_shield=divine_shield
        self.reborn=reborn
        self.ds_status=False
        self.health_before_reborn=None
        
        
        
        
    def __eq__(self,other):
        return (self.attack == other.attack and
                self.health == other.health and
                self.name == other.name and
                self.owner == other.owner and
                self.taunt == other.taunt and
                self.divine_shield == other.divine_shield and
                self.reborn == other.reborn and
                self.ds_status == other.ds_status and
                self.health_before_reborn == other.health_before_reborn)

        
        
    def __str__(self):
        return (self.name+str(self.health)+str(self.divine_shield)+str(self.reborn))

    def battle(self,anothercard: "Minion")->str:
        
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
            if anothercard.health<=0 and anothercard.has_reborn():
                anothercard.health_before_reborn=anothercard.health
                anothercard.health=1
                anothercard.reborn=False
        elif anothercard.has_divine_shield():
            anothercard.ds_status=True
            anothercard.divine_shield=False
            self.ds_status=False
            self.health-=anothercard.attack
            if self.health<=0 and self.has_reborn():
                self.health_before_reborn=self.health
                self.health=1
                self.reborn=False
        else:
            self.health-=anothercard.attack
            anothercard.health-=self.attack
            anothercard.ds_status=False
            self.ds_status=False
            if self.health<=0 and self.has_reborn():
                self.health_before_reborn=self.health
                self.health=1
                self.reborn=False 
            if anothercard.health<=0 and anothercard.has_reborn():
                anothercard.health_before_reborn=anothercard.health
                anothercard.health=1
                anothercard.reborn=False          
        self.attack_time-=1
        
        return self.name+ " attack: "+anothercard.name
        
    def reverse(self,anothercard):
        if self.ds_status and anothercard.ds_status:
            self.divine_shield=True
            self.ds_status=False
            anothercard.divine_shield=True
            anothercard.ds_status=False
            
        elif self.ds_status:
            self.divine_shield=True
            self.ds_status=False
            if anothercard.health_before_reborn!=None:
                anothercard.health=anothercard.health_before_reborn
                anothercard.reborn=True
                anothercard.health_before_reborn=None
            else:
                anothercard.health+=self.attack
            
        elif anothercard.ds_status:
            anothercard.divine_shield=True
            anothercard.ds_status=False
            if self.health_before_reborn!=None:
                self.health=self.health_before_reborn
                self.reborn=True
                self.health_before_reborn=None
            else:
                self.health+=anothercard.attack
        else:
            self.health+=anothercard.attack
            anothercard.health+=self.attack
            if self.health_before_reborn!=None and anothercard.health_before_reborn!=None:
                self.health=self.health_before_reborn
                self.reborn=True
                anothercard.health=anothercard.health_before_reborn
                anothercard.reborn=True
                self.health_before_reborn=None
                anothercard.health_before_reborn=None
            elif self.health_before_reborn!=None:
                self.health=self.health_before_reborn
                self.reborn=True
                self.health_before_reborn=None
            elif anothercard.health_before_reborn!=None:
                anothercard.health=anothercard.health_before_reborn
                anothercard.reborn=True
                anothercard.health_before_reborn=None     
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

    def has_reborn(self):
        if self.reborn:
            return True
        else:
            return False
        
        
    def to_dict(self):
        pre_json={}
        pre_json["name"]=self.name
        pre_json["attack"]=self.attack
        pre_json["health"]=self.health
        pre_json["taunt"]=self.taunt
        pre_json["ds"]=self.divine_shield
        pre_json["reborn"]=self.reborn
        return pre_json
        