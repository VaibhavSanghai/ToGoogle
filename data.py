import pandas as pd
import plotly_express as p

df = pd.read_csv("dataNew.csv")
fig = p.scatter(df, x="date", y="cases", color="country", size_max=60, title="TO GOOGLE, yes!")
fig.show()
