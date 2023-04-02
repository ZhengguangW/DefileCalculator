import copy
from Minion import Minion
from Board import Board
minion1=Minion(3,4,"34","friendly",True)
minion2=Minion(1,2,"12","friendly")
minion3=Minion(1,1,"11","friendly")
minion4=Minion(6,4,"64","enemy")
minion5=Minion(3,3,"33","enemy",True)
minion6=Minion(3,2,"32","enemy")

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
        return True

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
                if (activate_defile((temp_board))):
                    return
        else:
            continue
    return
        

if board.check_termination()==False:
    activate_defile(board)
else:
    print("Initial State is Good for Defile!")




