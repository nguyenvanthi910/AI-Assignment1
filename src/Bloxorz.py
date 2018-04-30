#!/usr/bin/python
try:
    from State import *
    import FileHandler as file
except ImportError:
    from src.State import  *
    import src.FileHandler as file
import time
import curses
import threading as thread
import sys

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
        time.sleep(0.1)

class waiting(thread.Thread):
    def __init__(self, stop = False):
        thread.Thread.__init__(self)
        self.stop = stop
    def run(self):
        self.wait()

    def wait(self):
        t = 0.5;
        while not self.stop:
            for i in range(4):
                str = "Wating{0}".format("."*i)
                sys.stdout.write("\r\t%-12s  %12d s" % (str, t))
                sys.stdout.flush()
                time.sleep(0.5)
                t += 0.5


if __name__ == '__main__':
    m = '1'
    m = input("Input level: ")
    while(m != 'q'):
        try:
            map, block, ls, goalA, goalB = file.readFrom(get_web_map(int(m)))

            initState = State(block, 0, map, True)
            initState.lsGoal = getLsGoal(ls, map)
            if goalA:
                initState.goalA = goalA
            if goalB:
                initState.goalB = goalB
            t = "1"
            print("\nALGORITHM LIST:\n\t1. Breadth first search\n\t2. Depth first search\n\t3....\r")
            t = input("Please input algorithm(default 1):")
            stop = False
            thread1 = waiting(stop)
            thread1.start()
            if t == "1":
                state = breadth_first_search(initState)
            elif t == "2":
                depth = input("Input max depth (default 10): ")
                try: d = int(depth)
                except Exception: d = 10
                state = depth_first_search(initState, d)
            elif t == "3":
                t = "fail"
            else: state = breadth_first_search(initState)

            thread1.stop = True
            curses.wrapper(printSolusion, state)
            m = input("Input another level (q for quit): ")
        except Exception as e:
            print(e)
            m = input("This level is error. Choose another level(q for quit): ")