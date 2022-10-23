import numpy as np
import pandas as pd
df = pd.read_csv('example')
print(df)
# df.to_csv('my_output',index=False)
# dfo = pd.read_csv('my_output')
# print(dfo)
#Excel
dfe = pd.read_excel('Excel_Sample.xlsx')
print(dfe)
dfe.to_excel('Excel_Sample2.xlsx',index=False)
# dfeo = pd.read_excel("Excel_Sample2.xlsx")
# print(dfeo)