import plotly.figure_factory as ff
import pandas as pd
import csv

df = pd.read_csv("/Users/kanuvanshkavi/Desktop/Kavi_Arora_Mac/Kavi_Projects3/Projects/Proj108/data.csv")
print(df.mean())
fig = ff.create_distplot([df["Avg_Rating"].tolist()], ["Average Rating"])
fig.show()