import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('./jetrail/jetrail.csv', nrows=10)
# print(df.head())
# print(df.shape)
df['Timestamp'] = pd.to_datetime(df['Datetime'], format='%d-%m-%Y %H:%M')  # 4位年用Y，2位年用y
df.index = df['Timestamp']
print(df)
