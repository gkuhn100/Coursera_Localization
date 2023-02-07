import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt

# Store the voltage and current data as column vectors.
I = np.array([[0.2, 0.3, 0.4, 0.5, 0.6]]).T
V = np.array([[1.23, 1.38, 2.06, 2.47, 3.17]]).T

plt.scatter(I,V)
plt.xlabel('Current (A)')
plt.ylabel('Voltage (V)')
plt.grid('True')

# Define the H matrix - what does it contain?
# H = ...
H  = I
y  = V
# Now estimate the resistance parameter.
# R = ... 
R = np.dot(np.dot(inv(np.dot(H.T,H)),H.T),y)

print('The slope parameter of the best-fit line (i.e., the resistance) is:')
print(R)

I_line = np.arange(0, 0.8, 0.1).reshape(8, 1)
V_line = R * I_line

plt.scatter(I,V)
plt.plot(I_line,V_line)
plt.xlabel('Current')
plt.ylabel('Voltage')
plt.grid(True)
