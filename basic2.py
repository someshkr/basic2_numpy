import numpy as np
import matplotlib.pyplot as plot
from numpy import pi
'''
x = Asin(Θ + φ)

where 
x = time 
A amplitude
Θ anglular dispalcement  = wt w--> frequency
φ  phase shift

'''
#defining sine function
y = np.linspace(-10,10,10000)
f = np.sin(y)
plot.plot(y,f)
plot.title('Sine Wave')

#defining x,y Axes
plot.xlabel('y')
plot.ylabel('f = sin(y)')


plot.grid(True,which = 'both')
plot.axhline(y = 0, color = 'k')
plot.show()
