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
df = pd.DataFrame(randn(5,4),index='A B C D E'.split(),columns='W X Y Z'.split())
df['W']
df[['W','Z']]
# SQL Syntax (NOT RECOMMENDED!)
df.W
type(df['W'])
df['new'] = df['W'] + df['Y']
df.drop('new',axis=1)
df.drop('new',axis=1,inplace=True)
df.drop('E',axis=0)
df.loc['A']
df.iloc[2]
df.loc['B','Y']
df.loc[['A','B'],['W','Y']]

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

#Missing Data
d = {'A': [1,2,np.nan] , 'B': [5,np.nan, np.nan], 'C': [1,2,3]}
df1 = pd.DataFrame(d)
df1.dropna()
df1.dropna(axis=1)
df1.dropna(thersh=2)
df1.fillna(value='Fill')
df1['A'].fllna(value=df['A'].mean())

#Groupby
data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Sales':[200,120,340,124,243,350]}
df2=pd.DataFrame(data)
bycomp = df2.groupby('Company')
bycomp.mean()
bycomp.sum()
bycomp.std()
bycomp.sum().loc['FB']
df2.groupby('Company').sum().loc['FB']
df2.groupby('Company').count()
df2.groupby('Company').max()
df2.groupby('Company').min()
df2.groupby('Company').describe()
df2.groupby('Company').describe().transpose()
df2.groupby('Company').describe().transpose()['FB']

#Merging joining and concatenation
#concat
df9 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']},
                        index=[0, 1, 2, 3])
df8 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                        'B': ['B4', 'B5', 'B6', 'B7'],
                        'C': ['C4', 'C5', 'C6', 'C7'],
                        'D': ['D4', 'D5', 'D6', 'D7']},
                         index=[4, 5, 6, 7]) 
df7 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                        'B': ['B8', 'B9', 'B10', 'B11'],
                        'C': ['C8', 'C9', 'C10', 'C11'],
                        'D': ['D8', 'D9', 'D10', 'D11']},
                        index=[8, 9, 10, 11])
pd.concat([df9,df8,df7])
pd.concat([df9,df8,df7],axis=1)
left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
   
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                          'C': ['C0', 'C1', 'C2', 'C3'],
                          'D': ['D0', 'D1', 'D2', 'D3']})  

#Merge  
left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                        'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3']})
    
right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                               'key2': ['K0', 'K0', 'K0', 'K0'],
                                  'C': ['C0', 'C1', 'C2', 'C3'],
                                  'D': ['D0', 'D1', 'D2', 'D3']})
pd.merge(left, right, on=['key1', 'key2'])
pd.merge(left, right, how='outer', on=['key1', 'key2'])
pd.merge(left, right, how='right', on=['key1', 'key2'])
pd.merge(left, right, how='left', on=['key1', 'key2'])

#Join
left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                      index=['K0', 'K1', 'K2']) 

right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                    'D': ['D0', 'D2', 'D3']},
                      index=['K0', 'K2', 'K3'])
left.join(right)
left.join(right, how='outer')


