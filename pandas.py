from unittest import result
import numpy as np
import pandas as pd
from numpy.random import randn
#Series
labels=['a', 'b', 'c']
my_list = [10, 20, 30]
arr = np.array(my_list)
d={'a':10, 'b':20, 'c':30}
pd.Series(data=my_list)
pd.Series(data=my_list, index=labels)
pd.Series(arr)
pd.Series(d)
pd.Series(data = [sum, print, len])
ser1 = pd.Series([1,2,3,4], ['a','b', 'c', 'd'])
ser2 = pd.Series([1,2,3,4], ['a','z', 'c', 'd'])
ser1['a']
ser1 + ser2

#DataFrame-I

#DataFrame-II
np.random.seed(101)
df = pd.DataFrame(randn(5,4),['A','B','C','D'], ['W','X','Y','Z'])
print(df)
booldf = df>0
df[booldf]
df[df>0]
df['W']>0
df[df['W']>0]
df[df['Z']<0]
resultdf = df[df['W']>0]
resultdf['X']
df[df['W']>0]['x','Y']
