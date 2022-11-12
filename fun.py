import pandas as pd
import numpy as np
import chart_studio.plotly as py
from plotly import __version__
import matplotlib.pyplot as plt
print(__version__)
import cufflinks as cf
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)
cf.go_offline()
df3 = pd.DataFrame({'x':[1,2,3,4,5], 'y':[10,20,30,20,10], 'z':[5, 4, 3, 2, 1]})



df3.iplot(kind='surface')
plt.show()