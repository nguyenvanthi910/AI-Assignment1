#!/usr/bin/python
try:
    from State import *
    import FileHandler as file
except ImportError:
    from src.State import  *
    import src.FileHandler as file
import time
import curses
import os

def printSolusion(window, state):
    root = []
    root.append(state)
    parent = state.parent
    while parent:
        root.append(parent)
        parent = parent.parent
    root = reversed(root)
    for i in root:
        window.addstr(5,5,str(i))
        window.refresh()
        time.sleep(0.5)

if __name__ == '__main__':
    m = '1'
    m = input("Input level: ")
    while(m != 'q'):
        try:
            map, block, ls, goalA, goalB = file.readFrom(get_web_map(int(m)))

            initState = State(block, 0, map, True)
            initState.lsGoal = getLsGoal(ls, map)
            initState.goalA = getLsGoal(goalA, map)
            initState.goalB = getLsGoal(goalB, map)
            t = "1"
            print("\nALGORITHM LIST:\n\t1. Breadth first search\n\t2. Depth first search\n\t3. Best first search\n\t4. Fail. \r")
            t = input("Please input algorithm(default 1):")
            if t == "1":
                state = breadth_first_search(initState)
            elif t == "2":
                depth = input("Input max depth (default 50): ")
                try: d = int(depth)
                except Exception: d = 50
                state = depth_first_search(initState, d)
            elif t == "3":
                state = hill_climbing(initState)
            elif t == "4":
                t = "fail"
            else:
                stop = False
                state = breadth_first_search(initState)
            curses.wrapper(printSolusion, state)
            m = input("Input another level (q for quit): ")
            os.system('cls' if os.name == 'nt' else 'clear')
        except Exception as e:
            print(e)
            os.system('cls' if os.name == 'nt' else 'clear')
            m = input("This level is error. Choose another level(q for quit): ")