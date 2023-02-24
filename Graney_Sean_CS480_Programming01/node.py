import pandas as pd

class Node:
    def __init__(self,stateSpace, name, goal, parent, cost):
        self.name = name
        self.GOAL = goal
        self.stateSpace = stateSpace
        self.state = name == goal
        self.parent = parent
        self.children = self.setChildren()
        self.cost = cost
        self.totalCost = self.setTotalCost()
        self.estimate = self.setEstimate()

    # recursively finds total cost of path 
    def setTotalCost(self):
        if self.parent:
            return self.cost + self.parent.totalCost
        else:
            return 0
    
    def setEstimate(self):
        estimateData = self.stateSpace['estimateData']
        return estimateData[self.name][self.GOAL]
    
    # Parses state space for valid children of node
    def setChildren(self):
        drivingData = self.stateSpace['drivingData'].loc[self.name][self.stateSpace['drivingData'][self.name]>0]
        estimateData = self.stateSpace['estimateData']
        childrenNames = list(drivingData.index)
        children = {}

        for childName in childrenNames:
            if not self.parent or childName != self.parent.name:
               children[childName] = { 'drivingData': drivingData[childName],
                        'estimateData': estimateData[childName][self.GOAL]}
        return children
    
    


        

