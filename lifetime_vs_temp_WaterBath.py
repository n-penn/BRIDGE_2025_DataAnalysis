import csv 
import matplotlib.pyplot as plt
import numpy as np

date = "2025-08-21"
file = "data/" + date + "_LifetimeHistogram" + "/" + date + "_data.csv"

with open(file, "r") as datafile:
    data = csv.DictReader(datafile)
    Thermometer = []
    Tau_1 = []
    for row in data:
        Thermometer.append(float(row['heatbath']))
        Tau_1.append(float(row['tau_1']))

    plt.scatter(Thermometer, Tau_1)
    plt.title("Fluorescence Lifetime vs Temperature")
    plt.xlabel("Heat Bath Temperature (Celsius)")
    plt.ylabel("Tau 1")
    plt.grid()
    ax = plt.gca()
    #ax.set_xlim([5, 40])
    #ax.set_ylim([4.5, 6.5])
    #plt.show()
    plt.savefig("results/lifetime_vs_temp_HeatBath/" + date + "_ltvstemp_hb.jpg")