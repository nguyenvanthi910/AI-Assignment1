try:
    from src import Search
except ImportError:
    import Search

class MapProblem(Search.Problem):
    def __init__(self, init, goal):