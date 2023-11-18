import numpy as np

def kde(samples, h):
    pos = np.arange(-5, 5.0, 0.1)
    N= len(samples)
    estDensity = np.ndarray(shape=(N, 2), dtype=float)
    gkernel= lambda u: 1/np.sqrt((2*np.pi)**(1/2)*h)*np.exp(-1/2*(u/h)**2)
    for j in range(len(pos)):
        for i in range(N):
            estDensity[j][1] += gkernel(np.abs(pos[j]-samples[i]))
        estDensity[j][1] /= N
        estDensity[j][0] = pos[j]
    return estDensity
