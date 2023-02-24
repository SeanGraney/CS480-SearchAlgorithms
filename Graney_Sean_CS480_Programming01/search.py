import time
import node as tree
import frontierQueue as fq
from pprint import pprint

class Search:
    def __init__(self, INITIAL, GOAL, df):
        self.ROOT = INITIAL
        self.GOAL = GOAL

        self.stateSpace = df # adjacency matrix 
        self.frontier = fq.FrontierQueue(lambda x:-x)
        self.reached = {} # lookup table {name: <nodeObj>}
        self.solution = [] # final path (updated after goal is found)
        self.cost = 0 # final driving cost (updated after goal is found)
        self.currentAlgorithm = "" # used to swap between bfs and a*
    
    def greedy(self):
        startTime = time.time()
        self.currentAlgorithm = 'greedy'

        # Check if inputs exist or if the start node is the end node
        if self.ROOT not in self.stateSpace['drivingData'] or self.GOAL not in self.stateSpace['drivingData']:
            self.solution = ['NOT FOUND']
            self.cost = "N/A Miles"
        elif self.ROOT == self.GOAL:
            self.solution = [self.ROOT]
            self.cost = 0
        else:
            self.initializeRoot()
            while not self.solution:
                self.search('greedy')
            self.solution.reverse() # soluion list is built backwards, so for correct represection

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
        if self.ROOT not in self.stateSpace['drivingData'] or self.GOAL not in self.stateSpace['drivingData']:
            self.solution = ['NOT FOUND']
            self.cost = "N/A Miles"
        elif self.ROOT == self.GOAL:
            self.solution = [self.ROOT]
            self.cost = 0
        else:
            self.initializeRoot()
            while not self.solution:
                self.search('aStar')

            self.solution.reverse() # soluion list is built backwards, so for correct represection

        return ({
            'title': "A* Search",
            'path': self.solution,
            'numStates': len(self.solution),
            'numNodes': len(self.reached),
            'pathCost': self.cost,
            'time': (time.time()-startTime)
        })

    # Initialize root node and children
    def initializeRoot(self):
        self.reached[self.ROOT] = tree.Node(self.stateSpace, self.ROOT, self.GOAL, None, 0)
        children = self.reached[self.ROOT].children

        # children takes the form of {'IL': 
        #                               {
        #                                   'drivingData': XXX,
        #                                   'estimatedData': XXX
        #                               },
        #                            'IA': ...
        #                            }
        for k, v in children.items():
            self.reached[k] = tree.Node(self.stateSpace, k, self.GOAL, self.reached[self.ROOT], v['drivingData'])
            self.frontier.add((k, self.eval(v, 0)))

    def search(self, algorithm):

        # ---------- TESTING ----------- #
        # print("---------- "+ self.frontier.peek()[2].name+"->"+ self.frontier.peek()[0] +" ----------")
        # pprint(list(map(lambda x:[x[0], x[1], x[2].name, x[3]], self.frontier.data)))
        # print('\n')
        # ------------------------------ #

        bestFirstNode = self.reached[self.frontier.pop()[0]]

        # if bestFirstNode is the GOAL get solution
        if bestFirstNode.state:
            self.getSolution(bestFirstNode)
            return 1

        # loop through children nodes of the bestFirstNode add new Nodes accordingly
        for child in self.expand(bestFirstNode):
            if child.name not in self.reached or child.totalCost < self.reached[child.name].totalCost:
                childData = bestFirstNode.children[child.name]
                self.reached[child.name] = child
                self.frontier.add((child.name, self.eval(childData, bestFirstNode.totalCost)))

    def expand(self, node):
        children = []
        for k, v in node.children.items():
            children.append(tree.Node(self.stateSpace, k, self.GOAL, node, v['drivingData']))
        return children

    # returns different values depending on which algorithm called eval() 
    def eval(self, data, parentCost):
        if self.currentAlgorithm == 'greedy':
            return data['estimateData']
        elif self.currentAlgorithm == 'aStar':
            # adds both estimateData and drivingData
            return sum(data.values())+parentCost            

    # recursively gets path and total cost
    def getSolution(self, node):
        if node:
            print(str(node.name))
            self.solution.append(node.name)
            self.cost += node.cost
            self.getSolution(node.parent)
    
    # refreshes data structures between algorithms
    def reset(self):
        self.frontier.clear()
        self.reached = {} # lookup table
        self.solution = [] # alive list (linked list of nodes)
        self.cost = 0
        








    
