import csv
import matplotlib.pyplot as plt
import numpy as np
import glob
import colorsys
from scipy.ndimage import gaussian_filter1d

# change these
date = "2025-08-21"
normalized = True
preview = False

# setup
foldername = date + "_LifetimeHistogram"
filename = "FLIM_"

# open ascii .dat file, convert to csv and change european decimal formatting to american
def getdata(filenumber):
    newlines = []
    with open("data/" + foldername + "/" + filename + filenumber + ".dat", "r") as inputfile:
        input = [line.rstrip() for line in inputfile]
        for i in range(2, len(input)): #it starts at 2 to exclude the first lines
            line = input[i]
            if line != "":
                line = line.replace(",",".").replace("\t",",")
                newlines.append(line)
    data = csv.reader(newlines)

    # read new file and extract data
    lifetimes = []
    counts = []
    for row in data:
        lifetimes.append(float(row[0]))
        counts.append(float(row[3]))    # row 1: tau (from fastflim) row 2: I[1] row 3: I[2]
    return lifetimes, counts

# count number of files to analyze
NumFiles = 0
for path in glob.iglob("data/" + foldername + "/" + "*.dat"):
    NumFiles += 1

# get temperatures
with open("data/" + foldername + "/" + date + "_data.csv", "r") as datacsv:
    reader = csv.DictReader(datacsv)
    temps = []
    for row in reader:
        temps.append(float(row['thermometer']))

# create graph
for i in range(1, NumFiles+1):
    lifetimes, counts = getdata(str(i))
    
    # smooth
    smoothed_counts = gaussian_filter1d(counts, sigma=2)
    
    # NORMALIZE
    counts_normalized = []
    max_ct = max(smoothed_counts)
    for ct in smoothed_counts:
        counts_normalized.append(ct/max_ct)

    # plot (use smoothed_counts for regular and counts_normalized for normalized)
    if normalized==True:
        plt.plot(lifetimes, counts_normalized, label = temps[i-1], color=colorsys.hls_to_rgb((i-1)/(NumFiles+1),0.5,0.75)) # could do NumFiles alone but the pink makes it hard to see :)
    else:
        plt.plot(lifetimes, smoothed_counts, label = temps[i-1], color=colorsys.hls_to_rgb((i-1)/(NumFiles+1),0.5,0.75)) # could do NumFiles alone but the pink makes it hard to see :)

plt.title("Intensity")
plt.xlabel("lifetime (ns)")
plt.ylabel("counts ($10^3$)")
plt.grid()
plt.legend(title="Temps ($^{\circ}$C)")
#
if preview==True:
    plt.show()
else:
    if normalized==False:
        plt.savefig("results/intensity_histo_comparison/" + foldername + ".jpg", dpi=300)
    else:
        plt.savefig("results/normalized_intensity_histo_comparison/" + foldername + "_normalized.jpg", dpi=300)
