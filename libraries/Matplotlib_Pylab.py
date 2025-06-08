# Matplotlib
import matplotlib.pyplot as plt
#from matplotlib import pyplot as plt

#(x,y)    (5,10) (10,20)
# plot scatter
x=[5,10]
y=[10,20]
#plt.scatter(x,y)

#pylab
import pylab
import numpy as np

def soso(c) : 
    return c**2  + c**3 - 5

x = np.arange(-100,100,5)
y = soso(x)

pylab.scatter(x,y,c = "black",marker ="^" )
pylab.xlabel("Distance")
pylab.ylabel("Time")
pylab.title("speed")
pylab.savefig("The speed.pdf")
pylab.show() 
