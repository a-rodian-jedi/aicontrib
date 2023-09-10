from contrib.data_structures.trees import BehaviorTree
from contrib.data_structures.trees.behavior import *

def sara():
    print("Sara doesn't want to sing!")
    return False

def tegan():
    print("Tegan sings!")
    return True

bt = BehaviorTree("stormtrooper")
bt.create_root(Selector, name="find_performer")
inv_sara = bt.root.add_child(Inverter, name="invert_sara")
inv_sara.add_child(Action, name="sara", func=sara)
bt.root.add_child(Action, name="tegan", func=tegan)

result = bt()