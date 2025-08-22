import csv 
import matplotlib.pyplot as plt
import numpy as np
import colorsys

# edit
dates = ["2025-08-" + i for i in ["01","06","11","12","13","15","18","19","20","21"]]
preview = False
ages = [11,7,10,11,12,29,14,15,16,17]
today_date = "2025-08-22" # change to today's date to save the file

date_age_dict = dict(zip(dates,ages))
sorted_dict = {k: v for k, v in sorted(date_age_dict.items(), key=lambda item: item[1], reverse=True)} # sort by temperature order (descending) so colors look nicer
data_dict = {}
i=0
dates = list(sorted_dict.keys()) # get list of dates in temp order

for date in dates:
    i+=1
    data_dict[date] = {"thermometer":[],"tau_1":[]}
    file = "data/" + date + "_LifetimeHistogram" + "/" + date + "_data.csv"
    with open(file, "r") as datafile:
        data = csv.DictReader(datafile)
        for row in data:
            data_dict[date]['thermometer'].append(float(row['thermometer']))
            data_dict[date]["tau_1"].append(float(row['tau_1']))
    plt.plot(data_dict[date]["thermometer"], data_dict[date]["tau_1"], color=colorsys.hls_to_rgb((i-1)/(len(dates)+1),0.5,0.75), label = date_age_dict[date])


plt.suptitle("Fluorescence Lifetime vs Temperature", fontsize=18)
plt.title("Comparison of All Data", fontsize=10)
plt.xlabel("Thermometer Temperature (Celsius)")
plt.ylabel("Tau 1")
#ax = plt.gca()
#ax.set_xlim([0, 40])
#ax.set_ylim([0, 8])
plt.legend(title="Age of sample (days)")
plt.grid()
if preview==True:
    plt.show()
else:
    plt.savefig("results/lt_vs_temp_comparison_" + today_date + ".jpg")

