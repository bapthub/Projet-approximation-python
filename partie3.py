import matplotlib.pyplot as plt
import numpy as np
<<<<<<< HEAD
import scipy as sci
import sympy as sym
from scipy.optimize import least_squares
from sympy import *
import math
import random


x = Symbol('x')
y = Symbol('y')

def nuage_point():
    nb_pts = input("Please enter number of points ?\n")
    nb_pts = int(nb_pts)
    incertitude = input("Please enter the incertitude ?\n")
    precision = incertitude[::-1].find('.')
    if (precision == - 1):
        precision = 0
    incertitude = float(incertitude)

    print("Choose respective points a,b,c,d")
    a = input("a ? ")
    b = input("b ? ")
    c = input("c ? ")
    d = input("d ? ")
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    
    l_xi = random.sample(range(a,b), nb_pts)
    l_xi.sort()

    l_yi = []
    yo = round(random.uniform(c,d),precision)
    l_yi.append(yo)

    
    # Randomizer des valeurs de y tout en respectant la condition { abs(yi - yi+1) < incertitude }
    for i in range(1, nb_pts, 1):
        prev_y = l_yi[i - 1]
        
        yi = round(random.uniform(c,d), precision)
        if (abs(yi - prev_y) > incertitude):
            while(abs(yi - prev_y) > incertitude):
                yi = round(random.uniform(c,d), precision)
        l_yi.append(yi)

    print()
    print("Last")
    print(l_xi)
    print(l_yi)

    #calcul du polynôme
    mymodel = np.poly1d(np.polyfit(l_xi, l_yi, 2))
    myline = np.linspace(a, b, d)
    print("model = ", mymodel)
    plt.scatter(l_xi, l_yi)

    #Tracer le polynôme 
    plt.plot(myline, mymodel(myline))

    plt.show()

def exo7(l_xi, l_yi):
    print(l_xi)
    print(l_yi)


    mymodel = np.poly1d(np.polyfit(l_xi, l_yi, 2))
    myline = np.linspace(0, 6, 12)
    print("model = ", mymodel)
    plt.scatter(l_xi, l_yi)

    #Tracer le polynôme 
    plt.plot(myline, mymodel(myline))

    plt.show()


nuage_point()
    
#exo7([0,1,2,4,6],[7,4,2,14,12])
#read_points([(0,2),(1,1),(2,0),(3,-1),(4,-3),(6,-1),(7,0),(9,2),(11,4),(12,5),(15,7),(16,10),(17,8)(18,-3),(20,-10)])
=======
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
>>>>>>> 83ddaf799c4bb9cf341d29cb8b6bcc79b0f2e511
