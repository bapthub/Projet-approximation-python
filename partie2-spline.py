import matplotlib.pyplot as plt
import numpy as np
from sympy import *
from scipy.interpolate import *


fig, ax = plt.subplots()
ax.set(xlim=(0, 10), ylim=(0, 10))
ax.grid()

x = Symbol('x')
pas = 0.1
coordonnee = []
stop = False

def eval(f, t):return f.subs(x, t)

def onClick(event):
    try:
        x, y = event.xdata, event.ydata
        print(x, y)
        coordonnee.append((round(x, 2), round(y, 2)))
        plt.scatter(x, y, color="black", marker="x")
    except:
        print("Please click on the grid !")

def onKey(event):
    global stop
    if (event.key == "enter"):
        stop = True

while True:
    key = fig.canvas.mpl_connect('key_press_event', onKey)
    click = fig.canvas.mpl_connect('button_press_event', onClick)
    plt.pause(1)
    if (stop):
        break

def Lk(x, k, coordonnee):
    result = 1
    for i in range(len(coordonnee)):
        if (i != k):
            result *= (x - coordonnee[i][0]) / (coordonnee[k][0] - coordonnee[i][0])
    return result

X1 = [item[0] for item in coordonnee]
Y1 = [item[1] for item in coordonnee]

def cubic_spline(x1,y1):
    X = np.array(x1)
    Y = np.array(y1)
    tck, u = splprep([X, Y], s=0)
    unew = np.linspace(0, 1, 200)
    out = splev(unew, tck)
    plt.plot(X, Y, 'bo')
    plt.plot(out[0], out[1])
    plt.show()

cubic_spline(X1, Y1)
