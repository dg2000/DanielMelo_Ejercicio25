import numpy as np

import matplotlib.pyplot as plt

M = 1.989e30

G = 6.674e-11

def proba( v, r, alfa):

    cuerpo = v*v / (G*M)
    return cuerpo**(1.0 / (1-alfa))




pos = np.array([0.39, 1.0, 5.2], float)
per = np.array([1.0/(0.24*365*24*3600), 1.0/(1.0*365*24*3600), 1.0/(11.86*365*24*3600)], float)

vel = per*2.0*np.pi*pos


for i in range
