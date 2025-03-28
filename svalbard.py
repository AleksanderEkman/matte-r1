import pandas as pd

xl_file = pd.ExcelFile("Data.xlsx")

dfs = xl_file.parse('Sheet1')

time_list = dfs['Time'].tolist()
temperature_list = dfs['Temperatur (°C)'].tolist()

print("Time List:")
print(time_list)

print("Temperature List:")
print(temperature_list)