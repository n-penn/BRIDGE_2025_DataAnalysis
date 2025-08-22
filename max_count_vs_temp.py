import csv
import matplotlib.pyplot as plt
import numpy as np
import glob

date = "2025-08-21" # change this as needed

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
    
    # NORMALIZE

    counts_normalized = []
    max_ct = max(counts)
    for ct in counts:
        counts_normalized.append(ct/max_ct)


# graph of max count vs temp
most_common_lifetimes = []
for i in range(1, NumFiles+1):
    max_counts_cache = []
    lifetimes, counts = getdata(str(i))
    max_ct = max(counts)
    for ct in range(0,len(counts)):
        if counts[ct] == max_ct:
            max_counts_cache.append(lifetimes[ct]) # only does first one--could fix this to take the average or something
    avg_max = np.average(max_counts_cache)
    most_common_lifetimes.append(avg_max)
        


plt.plot(temps, most_common_lifetimes)

plt.title("Location of Peak Internsity vs. Temperature")
plt.xlabel("Temperature ($^\circ$C)")
plt.ylabel("Lifetime with Maximum Count (ns)")
plt.grid()
#plt.show()
plt.savefig("results/max_count_vs_temp/" + date + "_MaxCtVsTemp.jpg", dpi=300)
