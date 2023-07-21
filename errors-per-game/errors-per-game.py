import plotly.express as px

import pandas as pd

data = pd.read_csv('errors-per-game/year-by-year-averages.csv')
# print(data.head())  # Display the first 5 lines of loaded data

modern = data.query('Year >= 1920')

# Error per game by year
# fig = px.line(modern, x='Year', y='E', title='MLB Errors per Game by Year', markers=True)

# Error per game by year, with 5-year moving average
# modern['5yr'] = modern['E'].rolling(5).mean()
fig = px.line(modern, x='Year', y='5yr', title='MLB Errors per Game by Year', markers=True)

# Error/Chances per game by year
# modern['E/Ch'] = modern['E'] / modern['Ch']
# fig = px.line(modern, x='Year', y='E/Ch', title='MLB Errors per Chance by Year', markers=True)

fig.show()