import sys
import pandas as pd
import search as s

def main():
    args = sys.argv[1:]
    INITIAL = args[0]
    GOAL = args[1]

    # convert csv to dataframe
    df = {
        'drivingData': pd.read_csv('data/driving.csv', index_col=0),
        'estimateData': pd.read_csv('data/straightline.csv', index_col=0)
        }

    if len(args)!=2:
        print('ERROR: Not enough or too many input arguments.')
        exit(1)

    # algorithm controller
    search = s.Search(INITIAL, GOAL, df)
    greedySearch = search.greedy()
    search.reset()
    aStarSearch = search.aStar()
    toString(INITIAL, GOAL, greedySearch, aStarSearch)


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
        "Solution path: "+ ", ".join(data["path"]) +"\n"+
        "Number of states on path: "+ str(data["numStates"]) +"\n"+
        "Number of expanded Nodes: "+ str(data["numNodes"]) +"\n"+
        "Path cost: "+ str(data["pathCost"]) +"\n"+
        "Execution Time: "+ str(data['time']) +" seconds\n"
    )


if __name__ == '__main__':
    main()