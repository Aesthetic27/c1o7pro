import pandas as PD
import csv
import plotly.express as PE

DF = PD.read_csv("data.csv")
mean = DF.groupby(["student_id","level"],as_index=False) ["attempt"].mean()
Fig = PE.scatter(mean,x ="student_id",y ="level",size="attempt",color= "attempt")
Fig.show()
