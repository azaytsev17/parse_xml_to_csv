import pandas as pd
from datetime import datetime

def to_df(file):
    start_time = datetime.now()
    print(f'Start time for df: {start_time}')
    df = pd.read_csv(file)
    end_time = datetime.now()
    print(f'End time for df: {end_time}')
    return df

def to_excel(dataframe, output_file):
    start_time = datetime.now()
    print(f'Start time for excel: {start_time}')
    dataframe.to_excel(output_file)
    end_time = datetime.now()
    print(f'End time for excel: {end_time}')

if __name__ == '__main__':
    df = to_df('new.csv')
    #to_excel(df, 'new.xlsx') usually freezes pc