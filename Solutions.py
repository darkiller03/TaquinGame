import collections
from Operations import *
from Node import Node

class Solutions:

    @staticmethod
    def BreadthSolution(frame,cus):
        print("Breadth First Search : ")
        print(" The Starting Point : ")
        Operations.printConsole(frame)
        queue = collections.deque([Node(frame)])
        seen = set()
        L = Operations.Linear(queue[0].frame)
        seen.add(''.join(map(str, L)))
        while queue:
            node = queue.pop()
            if node.frame.solved:
                solution_path = list(node.path)
                aff = Affichage(cus.canva , cus.Lpic , cus.window)
                # aff.motion(solution_path)
                print("Solution is found after", len(solution_path), " steps")
                aff.motion(solution_path)
                return
            for move, action in node.frame.actions:
                child = Node(move(), node, action)
                L = Operations.Linear(child.frame)
                chain = ''.join(map(str, L))
                if chain not in seen:
                    queue.appendleft(child)
                    seen.add(chain)
        print("There is no solution !!!!")

    @staticmethod
    def DepthSolution(frame,cus):
        print("Depth First Search : ")
        print(" The Starting Point : ")
        Operations.printConsole(frame)
        queue = collections.deque([Node(frame)])
        seen = set()
        L = Operations.Linear(queue[0].frame)
        seen.add(''.join(map(str, L)))
        while queue:
            node = queue.pop()
            if node.frame.solved:
                solution_path = list(node.path)
                # Affichage.motion(solution_path)
                aff = Affichage(cus.canva , cus.Lpic , cus.window)
                # aff.motion(solution_path)
                print("Solution is found after", len(solution_path), " steps")
                aff.motion(solution_path)
                return
            for move, action in node.frame.actions:
                child = Node(move(), node, action)
                L = Operations.Linear(child.frame)
                chain = ''.join(map(str, L))
                if chain not in seen:
                    queue.append(child)
                    seen.add(chain)
        print("There is no solution !!!!")
