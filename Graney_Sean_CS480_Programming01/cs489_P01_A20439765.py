import sys
import pandas as pd
import search as s
from IPython.display import display

def main():
    args = sys.argv[1:]
    if len(args)!=2:
        print('ERROR: Not enough or too many input arguments.')
        exit(1)

    df = pd.read_csv('data/driving.csv', index_col=0)
    # data = list(df.loc['IL'][df['IL']>0].head().index) # get all neighbors of illinois 


    INITIAL = args[0]
    GOAL = args[1]
    search = s.Search(INITIAL, GOAL, df)

    toString(INITIAL, GOAL, search.greedy(), search.aStar())


def toString(INITIAL, GOAL, greedyData, aStarData):
    print(
        "Graney, Sean, A20439765 solution:\n"+
        "Initial state: "+ INITIAL +"\n"+
        "Goal sate: "+ GOAL +"\n\n"+
        dataString(greedyData) +"\n"+
        dataString(aStarData)
    )

def dataString(data):
    return(
        data["title"] +":\n"+
        "Solution path: "+ " ".join(data["path"]) +"\n"+
        "Number of states on path: "+ str(data["numStates"]) +"\n"+
        "Number of expanded Nodes: "+ str(data["numNodes"]) +"\n"+
        "Path cost: "+ str(data["pathCost"]) +"\n"+
        "Execution Time: "+ str(data['time']) +" seconds\n"
    )


if __name__ == '__main__':
    main()