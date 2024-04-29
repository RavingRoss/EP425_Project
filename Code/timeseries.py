import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('results_24-02-06/Time-Series.txt',skiprows=1)

x = data[:,0]
y = data[:,1]

bbox_props = dict(boxstyle="round", fc="lightblue", ec="black", lw=2)

plt.plot(x,y,color='red',label='GD 358',zorder=2)
plt.scatter(x,y,c='black',s=5,zorder=3)
plt.text(4, .07, "15 peaks shown over 2.8 hours", ha="center", va="center", bbox=bbox_props, fontsize=8, color='black')
plt.grid(zorder=0)
plt.suptitle('Time Series')
plt.title('from BJD 2460347.85119493 to 2460347.97234762',fontstyle='oblique',fontsize=9)
plt.ylabel('Amplitude(mag)')
plt.xlabel('Kilo-Seconds (ks)')
plt.legend(loc='best')
plt.savefig('results_24-02-06/py-TimeSeriesPlot-mags')
plt.show()