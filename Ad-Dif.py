import numpy as np
from numpy import arange
from matplotlib import pyplot as plt
#Solving the time-independent advection-diffusion equation
k = 1.0
c = 1.0

def AdDif(r,t):
	u = r[0]
	y = r[1]
	return np.array([fu,k*k*fy],float)
phi = 1.0
a = 0.0
b = 10.0
N = 1000
h = (b-a)/N

tpoints = arange(a,b,h)
xpoints = []
ypoints = []
r = np.array([phi,1.0],float)
for t in tpoints:
	xpoints.append(r[0])
	ypoints.append(r[1])
	k1 = h*AdDif(r)
	k2 = h*AdDif(r+0.5*k1)
	k3 = h*AdDif(r+0.5*k2)
	k4 = h*AdDif(r+k3)
	r += (k1+2*k2+2*k3+k4)/6
plt.plot(tpoints,xpoints)
plt.plot(tpoints,ypoints)
plt.xlabel("t")
plt.savefig("Ad-Dif.png")
plt.show()
