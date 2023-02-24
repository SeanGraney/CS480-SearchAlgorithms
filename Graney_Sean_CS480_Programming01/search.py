import time
import node as tree
import frontierQueue as fq
from pprint import pprint

class Search:
    def __init__(self, INITIAL, GOAL, df):
        self.root = INITIAL
        self.GOAL = GOAL

        self.frontier = fq.FrontierQueue(lambda x:-x)
        self.reached = {} # lookup table
        self.solution = [] # alive list (linked list of nodes)
        self.stateSpace = df # adjacency matrix 
        self.cost = 0
        self.currentAlgorithm = ""
    
    def greedy(self):
        startTime = time.time()
        self.currentAlgorithm = 'greedy'
        self.initializeRoot()

        while not self.solution:
            self.search('greedy')
        self.solution.reverse()

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
        self.currentAlgorithm = 'aStar'
        self.initializeRoot()

        while not self.solution:
            self.search('aStar')
        self.solution.reverse()

        return ({
            'title': "A* Search",
            'path': self.solution,
            'numStates': len(self.solution),
            'numNodes': len(self.reached),
            'pathCost': self.cost,
            'time': (time.time()-startTime)
        })

    def initializeRoot(self):
        self.reached[self.root] = tree.Node(self.stateSpace, self.root, self.GOAL, None, 0)
        children = self.reached[self.root].children

        for k, v in children.items():
            self.reached[k] = tree.Node(self.stateSpace, k, self.GOAL, self.reached[self.root], v['drivingData'])
            self.frontier.add((k, self.eval(v, 0), self.reached[self.root], v))

    def search(self, algorithm):

        # ---------- TESTING ----------- #
        # print("---------- "+ self.frontier.peek()[2].name+"->"+ self.frontier.peek()[0] +" ----------")
        # pprint(list(map(lambda x:[x[0], x[1], x[2].name, x[3]], self.frontier.data)))
        # print('\n')
        # ------------------------------ #

        bestFirstNode = self.frontier.pop()
        bfName, bfEval, bfParent, bfData = bestFirstNode[0], bestFirstNode[1], bestFirstNode[2], bestFirstNode[3]

        if self.reached[bfName].state:
            self.getSolution(self.reached[bfName])
            return 1

        for child in self.expand(self.reached[bfName]):
            if child.name not in self.reached or child.totalCost < self.reached[child.name].totalCost:
                childData = self.reached[bfName].children[child.name]
                self.reached[child.name] = child
                self.frontier.add((child.name, self.eval(childData, self.reached[bfName].totalCost), self.reached[bfName], childData))

    def expand(self, node):
        children = []
        for k, v in node.children.items():
            children.append(tree.Node(self.stateSpace, k, self.GOAL, node, v['drivingData']))
        return children

    def eval(self, data, parentCost):
        if self.currentAlgorithm == 'greedy':
            return data['estimateData']
        elif self.currentAlgorithm == 'aStar':
            return sum(data.values())+parentCost            

    def getSolution(self, node):
        if node:
            self.solution.append(node.name)
            self.cost += node.cost
            self.getSolution(node.parent)
    
    def reset(self):
        self.frontier.clear()
        self.reached = {} # lookup table
        self.solution = [] # alive list (linked list of nodes)
        self.cost = 0
        








    
