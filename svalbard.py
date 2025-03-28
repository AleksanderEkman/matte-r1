import pandas as pd
import math
import matplotlib.pyplot as plt

xl_file = pd.ExcelFile("Data.xlsx")

dfs = xl_file.parse('Sheet1')

time_list = dfs['Time'].tolist()
temperature_list = dfs['Temperatur (°C)'].tolist()
skydekke_list = dfs['Skydekke (okta)'].tolist()

print("Time List:")
print(time_list)

print("Temperature List:")
print(temperature_list)

new_temp_list = []
new_time_list = []

for i, temp in enumerate(temperature_list):
    if not (math.isnan(temp) or temp == "nan" or (temp != temp)):
        new_temp_list.append(temp)
        new_time_list.append(temp)

print("New Time List:")
print(new_time_list)

print("New Temperature List:")
print(new_temp_list)
print('Skydekke List:')
print(skydekke_list)
