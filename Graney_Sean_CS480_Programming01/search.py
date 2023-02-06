import time
import node as tree
import frontierQueue as fq

class Search:
    def __init__(self, INITIAL, GOAL, df):
        self.root = INITIAL
        self.GOAL = GOAL

        self.frontier = fq.FrontierQueue(lambda x:-x)
        self.reached = {} # lookup table
        self.solution = [] # alive list (linked list of nodes)
        self.stateSpace = df # adjacency matrix 
        self.cost = 0
    
    def greedy(self):
        startTime = time.time()

        self.initializeRoot()

        return ({
            'title': "Greedy Best First Search",
            'path': self.solution,
            'numStates': len(self.solution),
            'numNodes': len(self.reached),
            'pathCost': self.cost,
            'time': (time.time()-startTime)
        })

    def aStar(self):
        startTime = time.time()

        self.initializeRoot()

        return ({
            'title': "A* Search",
            'path': self.solution,
            'numStates': len(self.solution),
            'numNodes': len(self.reached),
            'pathCost': self.cost,
            'time': (time.time()-startTime)
        })

    def initializeRoot(self):
        self.reached[self.root] = tree.Node(self.root, 'INITIAL', None, 0)
        self.reached[self.root].setChildren(self.stateSpace)
        children = self.reached[self.root].getChildren()

        for k, v in children.items():
            self.frontier.add((k, v))







    
