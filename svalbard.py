import pandas as pd
import math
import matplotlib.pyplot as plt
import numpy as np
import pylab

xl_file = pd.ExcelFile("Data.xlsx")
dfs = xl_file.parse('Sheet1')

time_list = dfs['Time'].tolist()
temperature_list = dfs['Temperatur (°C)'].tolist()
skydekke_list = dfs['Skydekke (okta)'].tolist()
dag_list = dfs['Dato'].tolist()
måned_list = dfs['Måned'].tolist()

sett_av_dager = set()

new_temp_list = []
new_time_list = []
new_skydekke_list = []
new_dag_list = []
new_måned_list = []

for time, temp, sky, dato, måned in zip(time_list, temperature_list, skydekke_list, dag_list, måned_list):
    if not math.isnan(temp) and not math.isnan(sky):
        if (måned, dato) not in sett_av_dager:
            sett_av_dager.add((måned, dato))  
            new_temp_list.append(temp)
            new_time_list.append(time)
            new_skydekke_list.append(sky)
            new_dag_list.append(dato)
            new_måned_list.append(måned)

print("Time List:")
print(new_time_list)
print("Temperature List:")
print(new_temp_list)
print('Skydekke List:')
print(new_skydekke_list)
print('Dag List:')
print(new_dag_list)
print('Måned List:')
print(new_måned_list)

print(len(new_temp_list))
print(len(new_dag_list))

print("Temp")

for i, temp in enumerate(new_temp_list):
    if i > 150 and i < 225:
        print(temp)

print("Dag")

for i, dag in enumerate(new_dag_list):
    if i > 150 and i < 225:
        print(dag)

print("Skydekke")

for i, sky in enumerate(new_skydekke_list):
    if i > 150 and i < 225:
        print(sky)



dager = []
for i in range(len(new_temp_list)):
    dager.append(i+1)

k = 15
glidende_avg = []
for i in range(k, len(new_temp_list)-k):
    glidende_avg.append(pylab.mean(new_temp_list[(i-k):(i+k)]))

xpoints = np.array(dager)
ypoints = np.array(new_temp_list)

glidende_avg_x = xpoints[k:len(new_temp_list) - k]

plt.plot(ypoints)
plt.plot(glidende_avg_x, glidende_avg, "k")
plt.show()
