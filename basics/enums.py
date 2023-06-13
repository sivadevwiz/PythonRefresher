# enums

from enum import Enum

# Enums are used to create constants

class State(Enum):
    INACTIVE = 0
    ACTIVE = 1


print("State.ACTIVE.....", State.ACTIVE)
print("State.INACTIVE.......", State.INACTIVE)
# .value only will give the value of the enum
print("State.ACTIVE.value.....", State.ACTIVE.value)
print("State.ACTIVE.name.......", State.ACTIVE.name)

print("State(0).........", State(0))
print("State(1).........", State(1))
# print(State(2)) # Error

print("State['ACTIVE'].........", State['ACTIVE'])  # State.ACTIVE
# print("State['ACTIVE'].........", State['Active']) # KeyError: 'Active'
# print("State('ACTIVE').........", State('ACTIVE')) # ValueError: 'ACTIVE' is not a valid State
print("State('1').........", State(1))  # State.ACTIVE
print("State('0').........", State(0))  # State.INACTIVE

print("list(State).....", list(State)) # [<State.INACTIVE: 0>, <State.ACTIVE: 1>]
print("len(State).....", len(State)) # 2
