import pandas as pd
import numpy as np

global x
x = 0

def cal_ema(close,step):
    global x
    x = (close * (2 / (step + 1)) + x*(1-(2/step+1)))
    return x

def first_ema(value):
    global x
    x = value
    return x


def calculate_ema(df,name,step,column_name):

    df[name] = np.nan
    df[name] = df['row_no'].apply(lambda x : np.nan if(x < step) else
    (first_ema(df[column_name].head(step).mean()) if(x==step) else cal_ema(df[column_name].iloc[x],step)))
    return df

def calculate_macd(step_1,step_2,step_3,df):
    first_ema = str(step_1)+'ema'
    second_ema = str(step_2)+'ema'
    signal = str(step_3)+'signal'
    df['row_no'] = df.index
    df = calculate_ema(df,first_ema,step_1,'Close')
    df = calculate_ema(df,second_ema,step_2,'Close')
    df['macd'] = df['row_no'].apply(lambda x: df[first_ema].iloc[x] - df[second_ema].iloc[x])
    df = calculate_ema(df,signal,step_2+step_3,'macd')
    df['histogram'] = df['macd'] - df[signal]
    print(df.head(100))
    return df


if __name__ == '__main__':
    df = pd.read_csv(r'C:\Users\AmanPc\Desktop\appl.csv')
    calculate_macd(12,26,9,df)
