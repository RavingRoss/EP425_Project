import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('results_24-02-06/P04_Spec.txt')

x = data[:,0]
y = data[:,1]
plt.figure(figsize=(11,4))
plt.scatter(x,y,c='black',s=.1,zorder=3)
plt.grid(zorder=0)
plt.title('F1 (F=1.42065, A=38.1957439, P=704.796)', fontsize=8)
plt.suptitle('Amplitude Spectrum')
plt.ylabel('Amplitude (mag)')
plt.xlabel('Frequency (mHz)')
plt.xticks(np.arange(0,7,step=0.5))
plt.savefig('results_24-02-06/P04_Amplitude_Spectrum')
plt.show()