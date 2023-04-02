import copy
from Minion import Minion
from Board import Board
from Owner_enum import owner
minion1=Minion(1,2,"12",owner.friendly)
minion2=Minion(1,3,"13",owner.friendly)
minion3=Minion(5,1,"51",owner.friendly)
minion4=Minion(1,1,"11",owner.enemy,True)
minion5=Minion(2,2,"22",owner.enemy,True)
minion6=Minion(3,4,"34",owner.enemy,True)

board=Board()
board.add_minion(minion1)
board.add_minion(minion2)
board.add_minion(minion3)
board.add_minion(minion4)
board.add_minion(minion5)
board.add_minion(minion6)
def activate_defile(board):
    if board.check_termination():
        print("One Possible Solution is:")
        board.printpath()
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
                activate_defile(temp_board)
        else:
            continue
    return
        

if board.check_termination()==False:
    activate_defile(board)
else:
    print("Initial State is Good for Defile!")




