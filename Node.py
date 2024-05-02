class Node: 

    def __init__(self , frame , parent=None, action = None):
        self.frame = frame
        self.parent = parent
        self.action = action


    @property
    def path(self):
        node , p = self, []
        while node:
            p.append(node)
            node = node.parent
        yield from reversed(p)