import copy
import sys
from Minion import Minion
from Board import Board
from Owner_enum import owner


a=Minion(1,3,"F1",owner.friendly,False,False,False)
b=Minion(2,3,"E1",owner.enemy,False,False,False)

c=Minion(1,3,"F1",owner.friendly,False,False,False)
d=Minion(2,3,"E1",owner.enemy,False,False,False)
print(b==c)
t1=Board(friendly=a,enemies=b)
l1=[t1]
t2=Board(friendly=c,enemies=d)
print(t1==t2)

print (t2 in l1)

def x():
    for i in range (1,4):
        for j in range (2,5):
            print(i,j)
            return
    return
x()