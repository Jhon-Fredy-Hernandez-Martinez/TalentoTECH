import matplotlib.pyplot as plt
import numpy as np
import math

a = 5
#print("This is just a test")
b = 2
c = a*b
cadena = 'This is just a test'

print(cadena)

#x = np.linspace(-3,3,50)
PI = math.pi
print("PI = ",PI)

x = np.linspace(0, 7.5*PI,1000)

y = np.cos(x)


plt.plot(x,y)
plt.grid()
plt.title('y=cos(x)')
plt.xlabel('x [rad]')
plt.ylabel('y')

