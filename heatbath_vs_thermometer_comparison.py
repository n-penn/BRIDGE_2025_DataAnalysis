# temperatures taken from https://www.wunderground.com/history/monthly/EDLW/date/2025-8

import csv 
import matplotlib.pyplot as plt
import numpy as np
import colorsys

# edit
dates = ["2025-08-" + i for i in ["01","06","11","12","13","15","18","19","20","21"]]
preview = False
outside_temps_max = [str(i) for i in [18,22,28,32,35,29,25,29,24,23]]
#outside_temps_avg = [str(i) for i in [16.1,16.8,21.2,24.2,27.2,23.4,19.2,21,18.3,17.5]]

date_outsidetemps_dict = dict(zip(dates,outside_temps_max))
sorted_dict = {k: v for k, v in sorted(date_outsidetemps_dict.items(), key=lambda item: item[1], reverse=True)} # sort by temperature order (descending) so colors look nicer
data_dict = {}
i=0
dates = list(sorted_dict.keys()) # get list of dates in temp order

for date in dates:
    i+=1
    data_dict[date] = {"heatbath":[],"thermometer":[]}
    foldername = date + "_LifetimeHistogram"
    file = "data/" + foldername + "/" + date + "_data.csv"
    with open(file, "r") as datafile:
        data = csv.DictReader(datafile)
        for row in data:
            data_dict[date]['thermometer'].append(float(row['thermometer']))
            data_dict[date]["heatbath"].append(float(row['heatbath']))
    plt.plot(data_dict[date]["heatbath"], data_dict[date]["thermometer"], color=colorsys.hls_to_rgb((i-1)/(len(dates)+1),0.5,0.75), label = date_outsidetemps_dict[date])

plt.suptitle("Measured Temperature vs. Set Temperature", fontsize=18)
plt.title("Comparison of All Data", fontsize=10)
plt.xlabel("Heat Bath Temperature (Celsius)")
plt.ylabel("Thermometer Temperature (Celsius)")
plt.legend(title="Highest recorded outdoor temp. on this day (Celsius)")
plt.grid()
ax = plt.gca()
ax.set_xlim([0, 50])
ax.set_ylim([0, 40])
if preview==True:
    plt.show()
else:
    plt.savefig("results/heatbath_vs_thermometer_comparison_2025-08-21.jpg")