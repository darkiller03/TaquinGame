import itertools
from Operations import Operations

class Frame:

    def __init__(self, state  , standard):
        self.state = state
        self.Lpic = standard.Lpic
        self.standard = standard


    @property
    def solved(self):
        sol = True
        comp = Operations.Linear2(self.standard.final_state)
        L = Operations.Linear(self)
        for i in range (len(L)):
            if (L[i]!=comp[i]):
                return False
        return sol

    @property 
    def actions(self):
        def create_move(From, to):
            return lambda: self.move(From, to)

        moves = []
        for i, j in itertools.product(range(3),
                                      range(3)):
            direcs = {'R':(i, j-1),
                      'L':(i, j+1),
                      'D':(i-1, j),
                      'U':(i+1, j)}

            for action, (r, c) in direcs.items():
                if r >= 0 and c >= 0 and r < 3 and c < 3 and \
                   self.state[r][c] == 0:
                    move = create_move((i,j), (r,c)), action
                    moves.append(move)
        return moves



    def move(self, From, to):
        copy = Frame(Operations.copy(self),self.standard)
        i, j = From
        r, c = to
        copy.state[i][j], copy.state[r][c] = copy.state[r][c], copy.state[i][j]
        return copy

    def firstFrameupdate(self):
        self.state = self.standard.first_state