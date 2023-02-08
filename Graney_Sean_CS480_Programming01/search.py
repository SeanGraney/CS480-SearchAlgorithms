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

        while not self.solution:
            self.expand()
        self.solution.reverse()
        print("solution: "+str(self.solution))

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
        self.reached[self.root] = tree.Node(self.root, self.getState(self.root), None, 0)
        self.reached[self.root].setChildren(self.stateSpace)
        children = self.reached[self.root].getChildren()

        for k, v in children.items():
            self.frontier.add((k, v, self.reached[self.root]))

    
    def expand(self):
        bestFirstNode = self.frontier.pop()
        bfName, bfCost, bfParent = bestFirstNode[0], bestFirstNode[1], bestFirstNode[2]
        print("name: "+bfName+
              " cost: "+str(bfCost)+
              " bfParent: "+bfParent.name)
        # Node has already been reached. If it exists see if path is better
        if bfName in self.reached:
            oldNode = self.reached[bfName]
            newParent = bfParent
            # if new path is better, otherwise do nothing

            if oldNode.getTotalCost() > (newParent.getTotalCost() + bfCost):
                oldNode.updateParent(bfParent, bfCost)
            return 0
        
        # Node had not yet been reached 
        # create node, add to reached
        newNode = tree.Node(bfName, self.getState(bfName), bfParent, bfCost)
        self.reached[bfName] = newNode

        # check if node is goal
        if newNode.getState() == "GOAL":
            self.cost = newNode.getTotalCost()
            self.getSolution(newNode)
            return 1

        # generate the children and add to frontier
        newNode.setChildren(self.stateSpace)
        children = newNode.getChildren()

        for k, v in children.items():
            self.frontier.add((k, v, newNode))
            
    
    def getState(self, name):
        if name == self.root:
            return "INITIAL"
        elif (name == self.GOAL):
            return "GOAL"
        else:
            return None  

    def getSolution(self, node):
        if node:
            self.solution.append(node.name)
            self.getSolution(node.parent)
        
        








    
