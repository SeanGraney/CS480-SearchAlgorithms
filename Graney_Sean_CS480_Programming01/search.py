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
        self.reached[self.root] = tree.Node(self.root, self.getState(self.root), None, 0)
        self.reached[self.root].setChildren(self.stateSpace['drivingData'])
        children = self.reached[self.root].getChildren()

        for k, v in children.items():
            self.frontier.add((k, self.eval(k, v), self.reached[self.root], v))
 
    def expand(self, algorithm):
        bestFirstNode = self.frontier.pop()
        bfName, bfEstimate, bfCost, bfParent = bestFirstNode[0], bestFirstNode[1], bestFirstNode[3], bestFirstNode[2]
        # print("name: "+bfName+
        #       " cost: "+str(bfCost)+
        #       " bfParent: "+bfParent.name)

        # Node has already been reached. If it exists see if path is better
        if bfName in self.reached:
            oldNode = self.reached[bfName]
            newCost = self.eval(bfParent.name, bfParent.getTotalCost()+bfEstimate)
            # if new path is better, otherwise do nothing
            if self.eval(oldNode.name, oldNode.getTotalCost()) > newCost:
                # print("old: "+str(oldNode.name)+" "+str(oldNode.cost)+"\n")
                # print("new: "+str(newParent.name)+" "+str((newParent.cost + bfCost)))
                oldNode.updateParent(bfParent, bfEstimate)
            return 0
        
        # Node had not yet been reached 
        # create node, add to reached
        newNode = tree.Node(bfName, self.getState(bfName), bfParent, bfEstimate)
        self.reached[bfName] = newNode

        # check if node is goal
        if newNode.getState() == "GOAL":
            # self.cost = newNode.getTotalCost()
            self.getSolution(newNode)
            return 1

        # generate the children and add to frontier
        newNode.setChildren(self.stateSpace['drivingData'])
        children = newNode.getChildren()

        for k, v in children.items():
            self.frontier.add((k, self.eval(k, v), newNode, v))

    def eval(self, name, cost):
        if self.currentAlgorithm == 'greedy':
            return cost
        elif self.currentAlgorithm == 'aStar':
            print("hit")
            estimateDf = self.stateSpace['estimateData']
            estimate = estimateDf[name][self.GOAL]
            return cost + estimate            
    
    def getState(self, name):
        if name == self.root:
            return "INITIAL"
        elif (name == self.GOAL):
            return "GOAL"
        else:
            return None  

    def getSolution(self, node):
        if node:
            a = self.solution.append(node.name)
            self.cost += node.cost
            self.getSolution(node.parent)
    
    def reset(self):
        self.frontier.clear()
        self.reached = {} # lookup table
        self.solution = [] # alive list (linked list of nodes)
        self.cost = 0
        








    
