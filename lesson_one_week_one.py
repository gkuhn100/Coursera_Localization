
import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt

I = np.array([[.2,.3,.4,.5,.6]]).T
V = np.array([[1.23,1.38,2.06,2.47,3.17]]).T
R = np.divide(V,I)
plt.scatter(I,V)
plt.title('Current vs Voltage Measurements with a bad Multimeter')
plt.xlabel('Current (A)')
plt.ylabel('Voltage (V)')
plt.grid(True)
plt.show()

H = np.ones((5,1),dtype = int)
Rhat = np.dot(np.dot(inv(np.dot(H.T,H)),H.T),R)
It = np.arange(0,1,.1).reshape(10,1)
Vt = Rhat * It
plt.scatter(I,V)
plt.plot(It,Vt)
plt.title('Current vs Voltage Measurements with a bad Multimeter')
plt.xlabel('Current (A)')
plt.ylabel('Voltage (V)')
plt.grid(True)
plt.show()
