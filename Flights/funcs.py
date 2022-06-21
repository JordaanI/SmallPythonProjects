import pandas as pd
import matplotlib.pyplot as plt

def split_dataframe(df,num):
    if num >= 1949 and num <= 1960:
        return df.loc[df.Date.dt.year == num]
    elif num > 0 and num < 13:
        return df.loc[df.Date.dt.month == num]
    else:
        print('Please select valid number')

def simple_plot(df,num):
    temp_frame = split_dataframe(df=df,num=num)
    plt.bar('Date', 'passengers', data=temp_frame)

