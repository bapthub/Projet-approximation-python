import matplotlib.pyplot as plt
import numpy as np

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

