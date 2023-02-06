import time

class Search:
    def __init__(self, INITIAL, GOAL):
        self.INITIAL = INITIAL
        self.GOAL = GOAL

        # self.frontier = priorityQueue
        self.reached = {} # lookup table
        self.solution = [] # alive list
        self.stateSpace = [] # adjacency matrix
        self.cost = 0
    
    def greedy(self):
        startTime = time.time()
        return ({
            'title': "Greedy Best First Search",
            'path': self.solution,
            'numStates': len(self.solution),
            'numNodes': len(self.reached),
            'pathCost': self.cost,
            'time': (startTime-time.time())
        })

    def aStar(self):
        startTime = time.time()
        return ({
            'title': "A* Search",
            'path': self.solution,
            'numStates': len(self.solution),
            'numNodes': len(self.reached),
            'pathCost': self.cost,
            'time': (startTime-time.time())
        })




    
