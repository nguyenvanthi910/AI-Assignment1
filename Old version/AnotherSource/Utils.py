def Stack():
    return []

class Queue():
    """
    Abstract class for three types:
        FIFO()
        PriorityQueue()
    Method is:
        append(item)
        extend(items)
        pop()
        len()
    """
    def __init__(self):
        ...
    def pop(self):...
    def append(self, item): ...
    def extend(self, items):
        for item in items:
            self.append(item)
    def pop(self):...
    def __len__(self):...

class FIFO():
    def __init__(self):
        self.ls = list()
        self.start = 0
    def append(self, item):
        self.ls.append(item)
    def __len__(self):
        return len(self.ls)
    def extend(self, items):
        self.ls.extend(items)
    def pop(self):
        self.ls.pop(0)
class PriorityQueue(Queue):
    def __init__(self, order = min, f = lambda x:x):
        self.ls = []
        self.order = order
        self.f = f
    def append(self, item):
        bisect.