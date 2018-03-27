import pandas as pd
import numpy as np

station_angles = pd.read_csv("http://rapid-hub.org/data/angles_UCI_CS.csv")
station_angles.columns = station_angles.columns.str.strip()
station_angles["cosine_values"] = station_angles["angle_degrees"].apply(np.cos)

print("Station_ID Angle Cosine_Value")

for index, row in station_angles.iterrows():
    print("{:>10.0f} {:>5} {:>12.05f}".format(row["station_id"], row["angle_degrees"], row["cosine_values"]))