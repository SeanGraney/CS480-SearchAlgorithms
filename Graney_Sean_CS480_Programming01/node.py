import pandas as pd

class Node:
    def __init__(self, df, name, goal, parent, cost):
        self.name = name
        self.GOAL = goal
        self.df = df
        self.state = name == goal
        self.parent = parent
        self.children = self.setChildren()
        self.cost = cost
        self.totalCost = self.setTotalCost()
        self.estimate = self.setEstimate()
    
    def setTotalCost(self):
        if self.parent:
            return self.cost + self.parent.totalCost
        else:
            return 0
    
    def getTotalCost(self):
        return self.totalCost
    
    def setEstimate(self):
        estimateData = self.df['estimateData']
        return estimateData[self.name][self.GOAL]

    def updateParent(self, newParent, newCost):
        self.parent = newParent
        self.cost = newCost
        self.totalCost = self.setTotalCost()
    
    def getParent(self):
        return self.parent
    
    def setChildren(self):
        drivingData = self.df['drivingData'].loc[self.name][self.df['drivingData'][self.name]>0]
        estimateData = self.df['estimateData']
        childrenNames = list(drivingData.head().index)
        children = {}
        for childName in childrenNames:
            if not self.parent:
               children[childName] = { 'drivingData': drivingData[childName],
                        'estimateData': estimateData[childName][self.GOAL]}
            elif childName != self.parent.name: 
                children[childName] = { 'drivingData': drivingData[childName],
                         'estimateData': estimateData[childName][self.GOAL]}
        return children
    
    def getState(self):
        return self.state
    


        

