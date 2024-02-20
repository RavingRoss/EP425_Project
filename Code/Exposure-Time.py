from sympy import *
import numpy as np
V = 13.65 # mag
a = 1/2 # m
area = (np.pi*(a)**2)
Q = 0.6
f = 3640*10**(-0.4*V)
d_lambda = 0.16
N = 1.508*10**7*(Q*area*f*d_lambda) # e/s
print(N)
#A = 1
#B = 63.9
#C = 616
#t = 72.4 # s
A_R = 2.5 # pixels
rho = 9 # e/pixel/s read noise
d = 3 # e/pixel/s
b = 1.4 # e/pixel/s

A = (N**2)/(230**2)
print('A = ',A)
B = (N+(np.pi*(3.5**2)*2*(b+d)))
print('B = ',B)
C = np.pi*(3.5**2)*2*(rho)**2
print('C = ',C)
t = ((B+np.sqrt(B**2+4*A*C))/(2*A))
print('t = ',t)