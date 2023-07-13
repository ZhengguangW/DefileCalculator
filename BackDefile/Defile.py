import copy
import sys
from BackDefile.Minion import Minion
from BackDefile.Board import Board
from BackDefile.Owner_enum import owner
# minion1=Minion(1,2,"12",owner.friendly)
# minion2=Minion(3,4,"34",owner.friendly)
# minion3=Minion(2,3,"23",owner.friendly)
# minion4=Minion(1,5,"15",owner.friendly)
# minion5=Minion(3,4,"34",owner.friendly)
# minion6=Minion(5,6,"56",owner.friendly)
# minion7=Minion(1,7,"17",owner.friendly)
# minion8=Minion(4,3,"43",owner.enemy)
# minion9=Minion(3,2,"32",owner.enemy)
# minion10=Minion(3,9,"39",owner.enemy)
# minion11=Minion(4,5,"45",owner.enemy)
# minion12=Minion(6,7,"67",owner.enemy)
# minion13=Minion(2,2,"22",owner.enemy)
# minion14=Minion(3,3,"33",owner.enemy)



board=Board()
# board.add_minion(minion1)
# board.add_minion(minion2)
# board.add_minion(minion3)
# board.add_minion(minion4)
# board.add_minion(minion5)
# board.add_minion(minion6)
# board.add_minion(minion7)
# board.add_minion(minion8)
# board.add_minion(minion9)
# board.add_minion(minion10)
# board.add_minion(minion11)
# board.add_minion(minion12)
# board.add_minion(minion13)
# board.add_minion(minion14)

class Calculate():
    
    def __init__(self):
        self.solution=None
        self.scenes=[]
        
    
    def get_scenes(self,board):
        self.scenes=[]
        self.scenes.append(board.prepare_json())
        for step in self.solution:
            friendly=None
            enemy=None
            friendly_name=step.split(" ")[0]
            enemy_name=step.split(" ")[2]
            for friendly_minion in board.friendly:
                if friendly_minion.name==friendly_name:
                    friendly=friendly_minion
            for enemy_minion in board.enemies:
                if enemy_minion.name==enemy_name:
                    enemy=enemy_minion
            friendly.battle(enemy)
            self.scenes.append(board.prepare_json())
            
            

    def activate_defile(self,board):
        if self.solution!=None:
            return 
      
        if board.check_termination():
            print("One Possible Solution is:")
            board.printpath()
            self.solution=board.printout
            return 

        for friendly in board.friendly:
            if friendly.left_attacktime():
                for enemy in board.enemies:
                    path=friendly.battle(enemy)
                    friendly_copy=[copy.deepcopy(x)for x in board.friendly]
                    enemy_copy=[copy.deepcopy(x)for x in board.enemies]
                    friendly.reverse(enemy)
                    temp_board=Board(initial=False,friendly=friendly_copy,enemies=enemy_copy)
                    temp_board.check_dead()
                    temp_board.printout=board.printout.copy()
                    temp_board.append_possible_printout(path)
                    self.activate_defile(temp_board) 
                    
        return 
            





