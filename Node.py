class Node: 

    def __init__(self , frame , parent=None, action = None,depth=0,cost=0):
        self.frame = frame
        self.parent = parent
        self.action = action
        self.depth = depth
        self.cost = cost 


    @property
    def path(self):
        node , p = self, []
        while node:
            p.append(node)
            node = node.parent
        yield from reversed(p)