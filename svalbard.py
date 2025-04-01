import pandas as pd
import math
import matplotlib.pyplot as plt
import numpy as np
import pylab

# Last inn Excel-fil
xl_file = pd.ExcelFile("Data.xlsx")
dfs = xl_file.parse('Sheet1')

# Konverter kolonner til lister
time_list = dfs['Time'].tolist()
temperature_list = dfs['Temperatur (°C)'].tolist()
skydekke_list = dfs['Skydekke (okta)'].tolist()
dag_list = dfs['Dato'].tolist()
måned_list = dfs['Måned'].tolist()

# Sett for å holde styr på hvilke datoer vi allerede har lagret
sett_av_dager = set()

# Nye lister med kun én oppføring per dag per måned
new_temp_list = []
new_time_list = []
new_skydekke_list = []
new_dag_list = []
new_måned_list = []

# Iterer gjennom dataen
for time, temp, sky, dato, måned in zip(time_list, temperature_list, skydekke_list, dag_list, måned_list):
    # Sjekk at verdiene ikke er NaN
    if not math.isnan(temp) and not math.isnan(sky):
        # Sjekk at vi ikke allerede har lagt til denne datoen i denne måneden
        if (måned, dato) not in sett_av_dager:
            sett_av_dager.add((måned, dato))  # Lagre datoen som brukt
            new_temp_list.append(temp)
            new_time_list.append(time)
            new_skydekke_list.append(sky)
            new_dag_list.append(dato)
            new_måned_list.append(måned)

# Skriv ut resultatene
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