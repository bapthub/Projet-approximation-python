import matplotlib.pyplot as plt
import numpy as np
from sympy import *

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

def polynomeLagrange(x, coordonnee):
    result = 0
    for k in range(len(coordonnee)):
        result += Lk(x, k, coordonnee) * coordonnee[k][1]
    return result

f = polynomeLagrange(x, coordonnee)

def tracer(f, start, end):
    X = np.arange(start, end + pas, pas)
    Y = [ eval(f, x) for x in X ]
    plt.title("Function " + str(f))
    plt.plot(X, Y)
    plt.axhline(0, color = "black")
    plt.axvline(0, color = "black")
    plt.grid()
    plt.show()


tracer(f, -10, 10)