from operator import attrgetter
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
        if minion.owner=="enemy":
            self.enemies.append(minion)
        if minion.owner=="friendly":
            self.friendly.append(minion)

    def check_dead(self):
        for minion in self.friendly:
            if minion.health<=0:
                self.friendly.remove(minion)
        for minion in self.enemies:
            if minion.health<=0:
                self.enemies.remove(minion)

    def get_enemies_maxhealth(self):
        enemy_max_health=max(self.enemies,key=attrgetter("health"))
        return enemy_max_health.health

    def check_termination(self):
        all=self.friendly+self.enemies
        all.sort(key=lambda x:x.health)
        all_index=self.get_enemies_maxhealth()
        all_health=[]
        for all_minion in all:
            all_health.append(all_minion.health)

        for i in range (1,all_index+1):
            try:
                if all_health[i-1]>i:
                    return False
            except:
                return False
        return True

    def append_possible_printout(self,path):
        self.printout.append(path)

    def printpath(self):
        for path in self.printout:
            print(path)
        

