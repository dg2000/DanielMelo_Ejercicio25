import numpy as np

import matplotlib.pyplot as plt

M = 1.989e30

G = 6.674e-11

UA = 149597870700.0

def gauss(v, r, alfa):

    sigma = 20000e20
    r = r**(1-alfa)
    arriba = (G*M - v*v/r)*(G*M - v*v/r)/(2.0*sigma*sigma)
    

    return np.exp(-arriba)

    

graf = np.linspace(0.0, 10, 100)


pos = np.array([0.39, 1.0, 5.2], float)
per = np.array([1.0/(0.24*365.0*24.0*3600.0), 1.0/(1.0*365.0*24.0*3600.0), 1.0/(11.86*365.0*24.0*3600.0)], float)

pos = UA*pos

vel = per*2.0*np.pi*pos

v1 = 2.0*np.pi*per[0]*pos[0]

p = np.ones(len(graf))




for i in range(len(graf)):
        
    p[i] = p[i] * gauss(v1, pos[0], graf[i])
    

plt.plot(graf, p)
plt.show()

