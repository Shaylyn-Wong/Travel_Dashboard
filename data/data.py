import pandas as pd
import json 


path_to_data = "data/hk_tourism_synthetic_data.csv"
data = pd.read_csv(path_to_data, low_memory=False)

origin = pd.read_csv("data/hk_tourist_origin.csv")

with open("data/countries.geojson") as f:
    geojson = json.load(f)
