# Temperature-Dependent TCSPC Analysis
This code was written by Nat Penn at the Technical University of Dortmund to analyze data from working with Andreas Gruhn in the Medical/Biological Physics research group of Prof. Dr. Matthias Schneider. 

## File Structure
- scripts in the main folder
- nested in main folder, not included in the upload:
  - data
  - results

The "data" folder should include one folder for each full measurement titled "YYYY-MM-DD_LifetimeHistogram". Each of these folders should include the ASCII data of the histograms from SymPhoTime 64 titled "FLIM_1", numbers in ascending order. The csv should be titled "YYYY-MM-DD_data.csv" with the first line
> heatbath,thermometer,tau_1,tau_2
and the following lines with the temperature and fit data.

## Scripts (updated 20 Aug 2025)
- heatbath_vs_thermometer_comparison: plots the measured temperature of the water above the sample against the temperature of the heatbath, with the option to compare the lines by the outside temperature
- intensity_histo_comparison: compares the histograms in a folder. Includes option for normalization
- lifetime_vs_temp and lifetime_vs_temp_WaterBath: the scripts to compare the lifetime from the fit (tau_1) with the temperature
- lt_vs_temp_comparison: does the same as the previous, but takes the data from all folders
- max_count_vs_temp: takes data from histograms, finds the lifetime with the highest number of occurrences, and plots that against the temperature
