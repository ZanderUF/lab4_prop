# plot counting curve for selection of operating voltage
# lab 4 proprotional counters

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('counting_curve_data')

voltage = data[:,0]
counts = data[:,1]
error_counts = data[:,2]

plt.errorbar(voltage,counts,yerr=error_counts, fmt='o')
#plt.scatter(voltage,counts)
plt.xlabel('Voltage ($V$)')
plt.ylabel('Counts')

plt.xlim([850,2000])

plt.show()
