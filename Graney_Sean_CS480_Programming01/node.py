import pandas as pd

class Node:
    def __init__(self, name, state, parent, cost):
        self.name = name
        self.state = state
        self.parent = parent
        self.children = {}
        self.cost = cost
        self.totalCost = self.setTotalCost()
    
    def setTotalCost(self):
        if self.parent:
            return self.parent.getTotalCost() + self.cost
        else:
            return 0
    
    def getTotalCost(self):
        return self.totalCost
    
    def setChildren(self, df):
        data = df.loc[self.name][df[self.name]>0]
        childrenNames = list(data.head().index)
        for childName in childrenNames:
            self.children[childName] = data[childName]
    
    def getChildren(self):
        return self.children

        

