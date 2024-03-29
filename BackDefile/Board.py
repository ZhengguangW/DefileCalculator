from operator import attrgetter
from BackDefile.Owner_enum import owner
class Board:
    def __init__(self,initial=True,friendly=None,enemies=None,printout=None):
        if initial:
            self.friendly=[]
            self.enemies=[]
            self.printout=[]
        if initial==False:
            self.friendly=friendly
            self.enemies=enemies
            self.printout=[]
            
    def __eq__(self,other):
        result=False
        if self.friendly==other.friendly:
            if self.enemies==other.enemies:
                result=True
        return result


    def add_minion(self,minion):
        if minion.owner==owner.enemy:
            self.enemies.append(minion)
        if minion.owner==owner.friendly:
            self.friendly.append(minion)

    def check_dead(self):
        minions_to_remove = []
        for minion in self.friendly:
            if minion.health <= 0:
                print(str(minion))
                minions_to_remove.append(minion)
        for minion in minions_to_remove:
            self.friendly.remove(minion)

        minions_to_remove = []
        for minion in self.enemies:
            if minion.health <= 0:
                print(str(minion))
                minions_to_remove.append(minion)
        for minion in minions_to_remove:
            self.enemies.remove(minion)
    
    
    
    
    def get_enemies_maxhealth(self):
        enemy_max_health_list=[]
        for enemy_minion in self.enemies:
            print(str(enemy_minion))
            if enemy_minion.has_divine_shield() or enemy_minion.has_reborn():
                enemy_max_health_list.append(enemy_minion.health+1)
                print("no1")
            else:
                enemy_max_health_list.append(enemy_minion.health)
                print("no")
        print(enemy_max_health_list)
        return max(enemy_max_health_list)

    def check_termination(self):
        all_minions=self.friendly+self.enemies
        all_index=self.get_enemies_maxhealth()
        all_health=[]
        for all_minion in all_minions:
            if all_minion.has_divine_shield() and all_minion.has_reborn():
                all_health.append(all_minion.health+2)
                all_health.append(all_minion.health+1)
            elif all_minion.has_divine_shield():
                all_health.append(all_minion.health+1)
            elif all_minion.has_reborn():
                all_health.append(all_minion.health)
                all_health.append(all_minion.health+1)
            else:
                all_health.append(all_minion.health)
        all_health.sort()
        for i in all_minions:
            print(str(i))
        print("check")
        print(all_health)
        desired_sequence=range(1,all_index+1)
        if set(desired_sequence).issubset(set(all_health)):
            print(set(desired_sequence))
            print(all_health)
            for i in all_minions:
                print(str(i))
            return True
        else:
            return False

    def append_possible_printout(self,path):
        self.printout.append(path)

    def printpath(self):
        for path in self.printout:
            print(path)
        

    def prepare_json(self):
        self.all_minions=self.enemies+self.friendly
        return [minion.to_dict() for minion in self.all_minions]
        