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

#df[(df['W'>0]) and (df['Y']>1)] #Error
df[(df['W'>0]) & (df['Y']>1)]
df[(df['W'>0]) | (df['Y']>1)]
df.reset_index()
# df.reset_index(inplace=True) - for permanent reset
newind = 'CA NY WY OR CO'.split()
df['States'] = newind
df.set_index("States") 

#DataFrame-III
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)
df = pd.DataFrame(randn(6,2),hier_index,['A','B'])
df.loc['G1']
df.loc['G1'].loc[1]
df.index.names = ['Groups', 'Number']
df.loc['G2'].loc[2]['B']
df.xs('G1')
df.xs(1, level='Number')