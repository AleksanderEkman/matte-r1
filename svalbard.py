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
new_skydekke_list = []

for time, temp, sky in zip(time_list, temperature_list, skydekke_list):
    if temp == temp and sky == sky: # if temp and skydekke != nan
        new_temp_list.append(temp)
        new_time_list.append(time)
        new_skydekke_list.append(sky)

print("Time List:")
print(new_time_list)
print("Temperature List:")
print(new_temp_list)
print('Skydekke List:')
print(new_skydekke_list)