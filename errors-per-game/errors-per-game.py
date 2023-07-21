import plotly.express as px

import pandas as pd

data = pd.read_csv('errors-per-game/year-by-year-averages.csv')
# print(data.head())  # Display the first 5 lines of loaded data

modern = data.query('Year >= 1920')

fig = px.line(modern, x='Year', y='E', title='MLB Errors per Game by Year', markers=True)

fig.show()