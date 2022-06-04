import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("data.csv")
x = df["Height(Inches)"].tolist()

fig = ff.create_distplot([df["Height(Inches)"].tolist()], ["height"], show_hist = False)
fig.show()