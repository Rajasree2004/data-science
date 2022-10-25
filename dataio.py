import numpy as np
import pandas as pd
from sqlalchemy import create_engine
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

#HTML
# data = df = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')
# print(data[0].head())

#SQL
engine = create_engine('sqlite:///:memory:')
df.to_sql('my_table', engine)
dfs = pd.read_sql('my_table',con=engine)
print(dfs)