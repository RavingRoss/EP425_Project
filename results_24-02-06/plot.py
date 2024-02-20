import matplotlib.pyplot as plt
from sympy import *
import numpy as np
import pandas as pd

data = pd.read_csv('KS-measurements.csv')
df = pd.DataFrame(data)

x = df['Kilo Secs']
y = df['rel_flux_T1']

yarr = np.array(y)
yarr.sort()
max = [yarr[139],yarr[138],yarr[137],yarr[136],yarr[135],yarr[134],yarr[133],yarr[132],
	yarr[131],yarr[130],yarr[129],yarr[128],yarr[127],yarr[126],yarr[125],yarr[124]]

bbox_props = dict(boxstyle="round", fc="lightblue", ec="black", lw=2)

plt.plot(x,y,color='red',label='GD 358',zorder=2)
plt.scatter(x,y,c='black',s=5,zorder=3)
plt.text(4, .145, "15 peaks shown over 3.5 hours", ha="center", va="center", bbox=bbox_props, fontsize=8, color='black')
plt.grid(zorder=0)
plt.suptitle('Time Series')
plt.title('from BJD 2460347.85119493 to 2460347.97234762',fontstyle='oblique',fontsize=9)
plt.ylabel('Amplitude(mag)')
plt.xlabel('Kilo-Seconds (ks)')
plt.legend(loc='best')
plt.savefig('py-TimeSeriesPlot')
plt.show()
