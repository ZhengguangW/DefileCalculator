import copy
from Minion import Minion
from Board import Board
minion1=Minion(3,4,"蜘蛛坦克","enemy")
minion2=Minion(5,3,"黑心商贩","enemy")
minion3=Minion(3,5,"伊利斯逐星","friendly")

board=Board()
board.add_minion(minion1)
board.add_minion(minion2)
board.add_minion(minion3)

def activate_defile(board):
    if board.check_termination():
        board.printpath()
        return

    for friendly in board.friendly:
        for enemy in board.enemies:
            path=friendly.battle(enemy)
            friendly_copy=[copy.deepcopy(x)for x in board.friendly]
            enemy_copy=[copy.deepcopy(x)for x in board.enemies]
            friendly.reverse(enemy)
            temp_board=Board(initial=False,friendly=friendly_copy,enemies=enemy_copy)
            temp_board.check_dead()
            temp_board.printout=board.printout.copy()
            temp_board.append_possible_printout(path)
            activate_defile((temp_board))
    return
        

if board.check_termination()==False:
    activate_defile(board)
else:
    print("Initial State is Good for Defile!")




