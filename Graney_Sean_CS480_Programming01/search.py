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
        self.currentAlgorithm = ""
    
    def greedy(self):
        startTime = time.time()
        self.currentAlgorithm = 'greedy'
        self.initializeRoot()

        while not self.solution:
            self.expand('greedy')
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
            self.expand('aStar')
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
            self.frontier.add((k, self.eval(v), self.reached[self.root], v))

 
    def expand(self, algorithm):
        bestFirstNode = self.frontier.pop()
        
        bfName, bfEval, bfParent, bfData = bestFirstNode[0], bestFirstNode[1], bestFirstNode[2], bestFirstNode[3]
        print(bfName +" "+ bfParent.name)

        # Node has already been reached. If it exists see if path is better
        if bfName in self.reached:
            oldCost = self.reached[bfName].totalCost
            newCost = bfParent.totalCost + bfData['drivingData']
            print("Old Cost: "+str(oldCost)+" New Cost: "+str(newCost))
            # if new path is better, otherwise do nothing
            if oldCost > newCost:
                print('hit')
                # print("old: "+str(oldNode.name)+" "+str(oldNode.cost)+"\n")
                # print("new: "+str(newParent.name)+" "+str((newParent.cost + bfCost)))
                self.reached[bfName].updateParent(bfParent, bfData['drivingData'])
        else:
            #Node had not yet been reached 
            # create node, add to reached
            self.reached[bfName] = tree.Node(self.stateSpace, bfName, self.GOAL, bfParent, bfData['drivingData'])

        # check if node is goal
        if self.reached[bfName].state:
            self.getSolution(self.reached[bfName])
            return 1

        children = self.reached[bfName].children
        for k, v in children.items():
            self.reached[k] = tree.Node(self.stateSpace, k, self.GOAL, self.reached[bfName], v['drivingData'])
            self.frontier.add((k, self.eval(v), self.reached[bfName], v))
        
        # print(self.frontier.__repr__())

    def eval(self, data):
        if self.currentAlgorithm == 'greedy':
            return data['estimateData']
        elif self.currentAlgorithm == 'aStar':
            estimateDf = self.stateSpace['estimateData']
            estimate = estimateDf[name][self.GOAL]
            return cost + estimate            

    def getSolution(self, node):
        if node:
            # print(node.parent.name)
            self.solution.append(node.name)
            print(node.cost)
            self.cost += node.cost
            self.getSolution(node.parent)
    
    def reset(self):
        self.frontier.clear()
        self.reached = {} # lookup table
        self.solution = [] # alive list (linked list of nodes)
        self.cost = 0
        








    
