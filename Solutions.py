import collections
from Operations import *
from Node import Node
import time
import heapq


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
        start_time = time.time()
        while queue:           
            node = queue.pop()
            if node.frame.solved:
                end_time = time.time()
                passed_time = end_time - start_time
                solution_path = list(node.path)
                aff = Affichage(cus.canva , cus.Lpic , cus.window)
                # aff.motion(solution_path)
                print("Solution is found after", len(solution_path), " steps")
                print(f"The operation took {passed_time:.6f} seconds.")
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
        start_time = time.time()
        while queue:
            node = queue.pop()
            if node.frame.solved:
                end_time = time.time()
                passed_time = end_time - start_time
                solution_path = list(node.path)
                # Affichage.motion(solution_path)
                aff = Affichage(cus.canva , cus.Lpic , cus.window)
                # aff.motion(solution_path)
                print("Solution is found after", len(solution_path), " steps")
                print(f"The operation took {passed_time:.6f} seconds.")
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

    @staticmethod
    def AStarSolution(frame, cus):
        print("A* Search:")
        print("The Starting Point:")
        Operations.printConsole(frame)  # Ensure Operations is defined
        
        # Initialize priority queue with starting node
        start_node = Node(frame)
        priority_queue = [(start_node.cost, id(start_node), start_node)]
        heapq.heapify(priority_queue)
        
        seen = set()
        L = Operations.Linear(start_node.frame)
        seen.add(''.join(map(str, L)))
        
        start_time = time.time()
        while priority_queue:
            _, _, node = heapq.heappop(priority_queue)  # Pop node with lowest cost
            if node.frame.solved:
                end_time = time.time()
                passed_time = end_time - start_time
                solution_path = list(node.path)
                print("Solution found after", len(solution_path), "steps")
                print(f"The operation took {passed_time:.6f} seconds.")
                aff = Affichage(cus.canva, cus.Lpic, cus.window)
                aff.motion(solution_path)
                return
            
            for move, action in node.frame.actions:
                child = Node(move(), node, action, node.depth + 1, node.cost + 1)  # Increment depth and cost
                L = Operations.Linear(child.frame)
                chain = ''.join(map(str, L))
                if chain not in seen:
                    heapq.heappush(priority_queue, (child.cost, id(child), child))  # Push child to priority queue
                    seen.add(chain)
        print("There is no solution !!!!")  # This should be outside the loop

    @staticmethod
    def DepthSolutionL(frame, cus):
        print("Depth First Search : ")
        print(" The Starting Point : ")
        Operations.printConsole(frame)
        stack = [Node(frame)]
        seen = set()
        L = Operations.Linear(stack[0].frame)
        seen.add(''.join(map(str, L)))
        start_time = time.time()
        while stack:
            node = stack.pop()
            if node.frame.solved:
                end_time = time.time()
                passed_time = end_time - start_time
                solution_path = list(node.path)
                # Affichage.motion(solution_path)
                aff = Affichage(cus.canva, cus.Lpic, cus.window)
                # aff.motion(solution_path)
                print("Solution is found after", len(solution_path), " steps")
                print(f"The operation took {passed_time:.6f} seconds.")
                aff.motion(solution_path)
                return
            for move, action in node.frame.actions:
                child = Node(move(), node, action)
                L = Operations.Linear(child.frame)
                chain = ''.join(map(str, L))
                if chain not in seen:
                    stack.append(child)
                    seen.add(chain)
        print("There is no solution !!!!")