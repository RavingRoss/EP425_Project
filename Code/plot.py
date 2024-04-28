import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('results_24-02-06/KS-measurements.csv')
df = pd.DataFrame(data)

x = df['Kilo Secs']
y = df['rel_flux_T1']

bbox_props = dict(boxstyle="round", fc="lightblue", ec="black", lw=2)

plt.plot(x,y,color='red',label='GD 358',zorder=2)
plt.scatter(x,y,c='black',s=5,zorder=3)
plt.text(4, .145, "15 peaks shown over 3.5 hours", ha="center", va="center", bbox=bbox_props, fontsize=8, color='black')
plt.grid(zorder=0)
plt.suptitle('Time Series')
plt.title('from BJD 2460347.85119493 to 2460347.97234762',fontstyle='oblique',fontsize=9)
plt.ylabel('Flux Amplitude')
plt.xlabel('Kilo-Seconds (ks)')
plt.legend(loc='best')
plt.savefig('results_24-02-06/py-TimeSeriesPlot-flux')
plt.show()
