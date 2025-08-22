import csv 
import matplotlib.pyplot as plt
import numpy as np

# edit
date = "2025-08-21"
sample_age = 17 # days between passaging and measuring
preview = False

file = "data/" + date + "_LifetimeHistogram" + "/" + date + "_data.csv"

with open(file, "r") as datafile:
    data = csv.DictReader(datafile)
    Thermometer = []
    Tau_1 = []
    for row in data:
        Thermometer.append(float(row['thermometer']))
        Tau_1.append(float(row['tau_1']))

    plt.scatter(Thermometer, Tau_1)
    plt.suptitle("Fluorescence Lifetime vs Temperature", fontsize=18)
    plt.title("Sample Age: " + str(sample_age) + " Days", fontsize=10)
    plt.xlabel("Thermometer Temperature (Celsius)")
    plt.ylabel("Tau 1")
    plt.grid()
    if preview==True:
        plt.show()
    else:
        plt.savefig("results/lifetime_vs_temp/" + date + "_ltvstemp.jpg")