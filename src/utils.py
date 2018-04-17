import bisect
def Stack():
    return []

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
        
class PriorityQueue():
    def __init__(self, order = min, f = lambda x:x):
        self.ls = []
        self.order = order
        self.f = f
    def append(self, item):
        bisect.insort(self.ls, (self.f(item), item))
    def __len__(self):
        return len(self.ls)
    def extend(self, items):
        for item in items:
            self.append(item)
    def pop(self):
        if self.order == min:
            return self.ls.pop(0)[1]
        else:
            return self.ls.pop()[1]