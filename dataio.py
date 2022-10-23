import numpy as np
import pandas as pd
df = pd.read_csv('example')
print(df)
df.to_csv('my_output',index=False)
dfo = pd.read_csv('my_output')
print(dfo)