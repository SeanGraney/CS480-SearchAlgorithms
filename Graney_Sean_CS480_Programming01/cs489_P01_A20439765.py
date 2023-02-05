import sys
import pandas as pd

def main():
    args = sys.argv[1:]
    df = pd.read_csv('data/driving.csv')
    print(df.to_string())
    


if __name__ == '__main__':
    main()