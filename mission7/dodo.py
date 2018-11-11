import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,100, 0.1)
xplus = np.arange(0,200, 0.1)
y = np.empty(100*10*2)
step = 0.1
y[0] = 0
print(x)
try:
    pos = 0
    for i in np.nditer(x):
        y[pos+1] = step*np.sin((np.pi*(pos))/1000)
        pos += 1
    print(pos)
except:
    pass
print(y)


plt.subplot(111)   # grille 4x1, 1er graphique
plt.plot(xplus,y)
plt.show()
