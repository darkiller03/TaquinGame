from Solutions import Solutions

class Resolver:
    

    def __init__(self,first_frame,cus):
        self.first_frame = first_frame
        self.cus = cus


    def BFSearch(self):
        Solutions.BreadthSolution(self.first_frame,self.cus)


    def DFSearch(self):
        Solutions.DepthSolution(self.first_frame,self.cus)

