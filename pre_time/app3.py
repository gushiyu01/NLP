import pandas as pd
import numpy as np


animals = pd.DataFrame({'kind': ['cat', 'dog', 'cat', 'dog'], 'height': [9.1, 6.0, 9.5, 34.0],
                        'weight': [7.9, 7.5, 9.9, 198.0]})


print(animals)


res = animals.groupby('kind').agg(min_height=pd.NamedAgg(column='height', aggfunc='min'),
                                  max_height=pd.NamedAgg(column='height', aggfunc='max'),
                                  average_weight=pd.NamedAgg(column='weight', aggfunc=np.mean),)
print(res)

lis = [5, 8, 9, 6]
print(eval('111'))
