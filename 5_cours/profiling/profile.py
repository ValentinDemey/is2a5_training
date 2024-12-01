# pip install ydata-profiling

import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv("https://storage.googleapis.com/tf-datasets/titanic/train.csv")
pr = df.profile_report()

pr.to_file("titanic_data.html")

