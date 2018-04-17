from utils import *
class Problem(object):
    def __init__(self, init, goal = None):
        self.init = init
        self.goal = goal

    def suceessor(self, state): 
        """return (action, children)"""
        pass

    def isGoal(self, state):
        return self.goal == state

    def cost(self,c,state1,action,state2):
        """Return the cost of a solution path """
        return c + 1

    def value(self):
        """F in Hill-climbing"""
        pass 

class Node:
    def __init__(self, state, parent = None, action = None, cost = 0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.depth = 0

    def __repr__(self):
        return  "<Node %s>" % (self.state)

    def path(self):
        x, result = self, [self]
        while x.parent:
            result.append(x.parent)
            x = x.parent
        return result

    def expand(self, problem):
        return [Node(nextState, self, act, problem.cost(self.cost,self.state,act,nextState))
                for (act, nextState) in problem.suceessor(self.state)]

def tree_search(problem, dataType):
    dataType.append(Node(problem.init))
    while dataType:
        node = dataType.pop()
        if problem.isGoal(node.state):
            return node
        dataType.extend(node.expand(problem))
    return None

def depth_first_search_tree(problem):
    return tree_search(problem, Stack())

def breadth_first_search_tree(problem):
    return tree_search(problem, FIFO())

def best_first_search_tree(problem, order = min, f = lambda x : x):
    return tree_search(problem, PriorityQueue(order, f))
