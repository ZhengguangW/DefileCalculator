from operator import attrgetter
from Owner_enum import owner
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


    def add_minion(self,minion):
        if minion.owner==owner.enemy:
            self.enemies.append(minion)
        if minion.owner==owner.friendly:
            self.friendly.append(minion)

    def check_dead(self):
        for minion in list(self.friendly):
            if minion.health<=0:
                self.friendly.remove(minion)

        for minion in list(self.enemies):
            if minion.health<=0:
                self.enemies.remove(minion)

    def get_enemies_maxhealth(self):
        enemy_max_health_list=[]
        for enemy_minion in self.enemies:
            if enemy_minion.has_divine_shield():
                enemy_max_health_list.append(enemy_minion.health+1)
            else:
                enemy_max_health_list.append(enemy_minion.health)
        return max(enemy_max_health_list)

    def check_termination(self):
        all=self.friendly+self.enemies
        all_index=self.get_enemies_maxhealth()
        all_health=[]
        for all_minion in all:
            if all_minion.has_divine_shield():
                all_health.append(all_minion.health+1)
            else:
                all_health.append(all_minion.health)
        all_health.sort()
        desired_sequence=range(1,all_index+1)
        if set(desired_sequence).issubset(set(all_health)):
            print(set(desired_sequence))
            print(all_health)
            return True
            
        else:
            return False
        # for i in range (1,all_index+1):
        #     try:
        #         if all_health[i-1]>i:
        #             return False
        #     except:
        #         return False
        # return True

    def append_possible_printout(self,path):
        self.printout.append(path)

    def printpath(self):
        for path in self.printout:
            print(path)
        

