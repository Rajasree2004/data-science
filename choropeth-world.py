import pandas as pd
import plotly.io as pio
pio.renderers.default = 'notebook'
import chart_studio.plotly as py
import plotly.graph_objs as go

df = pd.read_csv("2014_World_GDP")
data = dict(
    type = 'choropleth',
    locations = df['CODE'],
    z = df['GDP (BILLIONS)'],
    text = df['COUNTRY'],
    colorbar = {'title': 'GDP in billion USD'}
)
layout = dict(title = '2014 Global GDP',
            geo = dict(showframe=False,
            projection={'type':'mercator'})
)
choro = go.Figure(data=[data], layout = layout)
choro.show()