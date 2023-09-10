from functools import partial

from contrib.data_structures.trees import BehaviorTree
from contrib.data_structures.trees.behavior import *

def try_door(state):
    state.update_data("door", "locked")
    print("The door is locked!")
    return False

def try_unlock():
    print("The Stormtrooper tries to unlock the door...")
    print("...but he doesn't have a key!")
    return False

def bash_door(state):
    print("The Stormtrooper rams his shoulder against the door!")
    print("...and the door breaks free!")
    state.update_data("door", "broken")
    state.update_data("trooper_hp", -5)
    return True

bt = BehaviorTree("stormtrooper")
bt.create_root(Selector, name="open_door")
bt.root.add_child(Action, name="try_door", func=partial(try_door, bt.root))
bt.root.add_child(Action, name="try_unlock", func=try_unlock)
bt.root.add_child(Action, name="bash_door", func=partial(bash_door, bt.root))

result = bt()