"""
File: PotholeFilling.py
Name: TODO:
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *


def main():
    """
    Pre-condition: Karel is at the (2, 1)
    post-condition: Karel is at the (2, 7)
    """
    for i in range(3):
        go_in()
        put_99_beeper()
        go_out()

def go_in():
    """
    Pre-condition: Karel is at upper left of the pothole, facing east
    post-condition: Karel is in the pothole, facing south
    """
    move()
    turn_right()
    move()


def go_out():
    """
    Pre-condition:  Karel is in the pothole, facing south
    post-condition: Karel is at upper left of the pothole, facing east
    """
    turn_around()
    move()
    turn_right()
    move()


def turn_right():
    """
    Karel will turn right
    """
    for i in range(3):
        turn_left()


def turn_around():
    """
    Pre-condition:  Karel is facing south
    post-condition: Karel is facing north
    """
    turn_left()
    turn_left()


def put_99_beeper():
    """
    Karel will put 99 beepers
    """
    for i in range(99):
        put_beeper()

# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
