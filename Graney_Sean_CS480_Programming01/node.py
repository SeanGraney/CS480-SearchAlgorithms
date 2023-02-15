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
            print("")
            return self.parent.totalCost + self.cost
        else:
            return 0
    
    def getTotalCost(self):
        return self.totalCost

    def updateParent(self, newParent, newCost):
        self.parent = newParent
        self.cost = newCost
        self.setTotalCost()
    
    def getParent(self):
        return self.parent
    
    def setChildren(self, df):
        data = df.loc[self.name][df[self.name]>0]
        childrenNames = list(data.head().index)
        for childName in childrenNames:
            if not self.parent:
               self.children[childName] = data[childName]
            elif childName != self.parent.name: 
                self.children[childName] = data[childName]
    
    def getChildren(self):
        return self.children
    
    def getState(self):
        return self.state
    


        

