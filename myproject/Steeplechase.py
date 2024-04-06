"""
File: Steeplechase.py
Name: TODO:
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()
            turn_left()


def jump():
    """
    precondition: Karel is on the left side of the wall, facing east
    postcondition: Karel is on the right side of the wall
    """
    up()
    cross()
    down()


def up():
    """
    precondition: Karel is on the left side of the wall, facing East
    precondition: Karel is facing North
    """
    turn_left()
    # Facing North
    while not right_is_clear():
        move()


def cross():
    """
    precondition: Karel is facing North
    precondition: Karel is at the upper right, facing South
    """
    turn_right()
    move()
    turn_right()


def down():
    """
    precondition: Karel is at the upper right, facing South
    postcondition: Karel is on the right side of the wall, facing South
    """
    while front_is_clear():
        move()


def turn_right():
    turn_left()
    turn_left()
    turn_left()



# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
