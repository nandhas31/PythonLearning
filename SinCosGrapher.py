import numpy
import matplotlib.pyplot as plt
i = -2*numpy.pi
x,y,z = [],[],[]

while(i <= 2*numpy.pi):
    x.append(i)
    y.append(numpy.sin(i))
    z.append(numpy.cos(i))
    i += numpy.pi/180

plt.plot(x,y)
plt.plot(x,z)
plt.show()
