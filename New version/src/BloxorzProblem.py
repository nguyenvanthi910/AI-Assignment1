import Search

class StateOfFindGoal():
    def __init__(self, current, lsPointAndState, map):
        """
        Point and State is (row, col, True | False | None)
            True is a button which is enabled.
            False is a button which is not enabled
            None is a goal point.
        """
        self.current = current
        self.lsPoint = lsPoint
        self.map = map
        self.newMap
    def expand(self):


class FindGoalBroblem(Search.Problem):
    def __init__(self, initial, goal = None):
        super().__init__(initial, goal)
    def isGoal(self, state):
        pass
    def cost(self, c, state1, action, state2)
        return c + 1
    

class BloxorzBroblem(Search.Problem):
    def __init__(self, initial, goal):
        super().__init__(initial, goal)
    
    def isGoal(self, state):
        super().isGoal(state)

    def cost(self, c, state1, action, state2):
        super().cost(c, state1, action, state2)
        
