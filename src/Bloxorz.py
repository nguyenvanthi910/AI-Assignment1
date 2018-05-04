#!/usr/bin/python
try:
    from State import *
    import FileHandler as file
except ImportError:
    from src.State import  *
    import src.FileHandler as file
import time
import curses
import sys

def printSolusion(window, args):
    state, counter, elapsed = args
    root = []
    root.append(state)
    parent = state.parent
    while parent:
        root.append(parent)
        parent = parent.parent
    root = reversed(root)
    if counter == -1:
        window.clear()
        window.addstr("\n\t\t%s\n" % state.getMap().name.upper())
        window.addstr("Solution not found.")
    else:
        for i in root:
            window.clear()
            window.addstr("\n\t\t%s\n" % i.getMap().name.upper())
            window.addstr("\n\tExplored %d states" % counter)
            window.addstr("\n\tMove %d steps" % state.value)
            window.addstr("\n\tElapsed %f s\n\n" % elapsed)
            window.addstr(str(i))
            window.addstr("\n\n")
            window.refresh()
            time.sleep(0.5)
        window.addstr("MOVE STEP: \n")
        window.addstr(getMoveStep(state))
    window.addstr("\nPress any key to continue...")
    window.getkey()
if __name__ == '__main__':
    if len(sys.argv) == 1:
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
                print("\nALGORITHM LIST:\n\t1. Breadth first search\n\t2. Depth first search\n\t3. Best first search\n\t")
                t = input("Please input algorithm(default 1):")
                elapsed = 0
                counter = 0
                if t == "1":
                    start = time.clock()
                    state, counter = breadth_first_search(initState)
                    elapsed = (time.clock()) - start
                elif t == "2":
                    depth = input("Input max depth (default 50): ")
                    try: d = int(depth)
                    except Exception: d = 50
                    start = time.clock()
                    state, counter = depth_first_search(initState, d)
                    elapsed = (time.clock()) - start
                elif t == "3":
                    start = time.clock()
                    state, counter = best_first_search(initState)
                    elapsed = (time.clock()) - start
                else:
                    start = time.clock()
                    state, counter = breadth_first_search(initState)
                    elapsed = (time.clock()) - start
                curses.initscr()
                curses.start_color()
                curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_WHITE)
                curses.init_pair(2, curses.COLOR_RED, curses.COLOR_WHITE)
                curses.wrapper(printSolusion, [state, counter, elapsed])
                m = input("Input another level (q for quit): ")
            except Exception as e:
                print(e)
                m = input("This level is error. Choose another level(q for quit): ")
    elif sys.argv[1] == 'runall': #Run Bloxorz.py runall
        result = '%30s%30s\n%10s%10s%10s%10s%10s%10s%10s\n' %\
                 ("BREADTH", "BEST", "LEVEL", "STATES", "STEPS", "TIME", "STATES", "STEPS", "TIME")
        fileResult = open('result.txt', mode='w')
        fileResult.write(result)
        fileResult.flush()
        result = ''
        for i in range(34)[1:]:
            map, block, ls, goalA, goalB = file.readFrom(get_web_map(i))
            initState = State(block, 0, map, True)
            initState.lsGoal = getLsGoal(ls, map)
            initState.goalA = getLsGoal(goalA, map)
            initState.goalB = getLsGoal(goalB, map)
            start = time.clock()
            s1, count1 = breadth_first_search(initState)
            elapsed = (time.clock()) - start
            result += '%10d%10d%10d%10f' % (i, count1, s1.value, elapsed)

            map, block, ls, goalA, goalB = file.readFrom(get_web_map(i))
            initState = State(block, 0, map, True)
            initState.lsGoal = getLsGoal(ls, map)
            initState.goalA = getLsGoal(goalA, map)
            initState.goalB = getLsGoal(goalB, map)
            start = time.clock()
            s2, count2 = best_first_search(initState)
            elapsed = (time.clock()) - start
            result += '%10d%10d%10f\n' % (count2, s2.value, elapsed)

            fileResult.write(result)
            fileResult.flush()
            result = ''
            print("level %d success\n" % i)
        fileResult.close()