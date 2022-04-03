import matplotlib.pyplot as plt
import numpy as np
from sympy import *
import math

x = Symbol('x')

def set_range(min,max,precision):
    return np.linspace(min, max, precision)

#plot(x ** 3 + 1, (x, -2, 2))

def plot_function(function, min, max):
    plot(function,(x, min, max))

def plot_fun_der(function, derivate, min, max):
    plot(function,derivate,(x, min, max))

def plot_fun_der_sec(function, derivate, second, min, max):
    plot(function, derivate, second, (x, min, max))

def plot_all(*args):
    t = len(args)
    if t < 3 or t > 5:
        return False
    if t == 3:
        plot(args[0],(x, args[1],args[2]))
    elif t == 4:
        plot(args[0], args[1],(x, args[2], args[3]))
    else:
        plot(args[0], args[1],args[2],(x, args[3], args[4]))

def derive(f):
    return diff(f, x, 1)

def derive_second(f):
    return diff(f, x, 2)

def evaluer(f, t):
    return f.subs(x, t)

def monotonie(f, a, b):
    y1 = evaluer(derive(f),a)
    y2 = evaluer(derive(f),b)
    if (y1 < 0 and y2 < 0):
        return "d"
    elif (y1 > 0 and y2 >0):
        return "c"
    return "n"

def forme_courbe(f,a,b):
    y1 = evaluer(derive_second(f), a)
    y2 = evaluer(derive_second(f), b)
    if (y1 < 0 and y2 < 0):
        return "concave"
    elif (y1 > 0 and y2 > 0):
        return "convexe"
    return "neutre"

def _lagrange(f, xo, b):
    xn = xo - (evaluer(f, xo) * (xo - b) / (evaluer(f, xo) - evaluer(f,b)))
    #xn = xo - (f.evalf(xo) * (xo - b) / (f.evalf(xo) - f.evalf(b)))
    last = xo
    i = 0
    while abs(xn - float(last)) > 0.01:
        last = xn
        xn = xn - evaluer(f,xn) * (xn - b) / (evaluer(f, xo) - evaluer(f,b))
        """print(xn)
        if i == 10:
            break
        i += 1"""
    return xn

def lagrange(f,a,b):
    fc = forme_courbe(f,a,b)
    f_a = evaluer(f,a)
    fs_a = evaluer(derive_second(f),a)
    if f_a * fs_a > 0:
        return _lagrange(f,a,b)
    else:
        return _lagrange(f,b,a)

#part 3
#2
# def plot_points(n,epsilion,a,b,c,d):
#     re

#3


# part 4
#2
def nuage_point(a,b,n,f):
    h = (b - a) / n
    l = []
    (xo,yo) = (a,f(a))
    l.append((xo,yo))
    for i in range(a + 1,n):
        (xi,yi) = (xo + h,f(xo + h))
        l.append((xi,yi))
        (xo,yo) = (xi,yi)
    (xn,yn) = (b,f(b))
    l.append((xn,yn))
    return l

#3
def integration_rectange_inf(a,b,n,l):
    h = (b - a) / n
    res = 0
    for i in range(len(l) - 1):
        res += l[i][1]
    return res * h

#3
def integration_rectange_sup(a,b,n,l):
    h = (b - a) / n
    res = 0
    for i in range(len(l)):
        res += l[i][1]
    return res * h

#4
def integration_trapeze(a,b,n,l):
    h = (b - a) / n
    new_l = l[1:]
    sum = 0
    for i in range(len(new_l) - 1):
        sum += new_l[i][1]
    fa = l[0][1]
    fb = l[len(l) - 1][1]
    return (h / 2) * (fa + fb + 2 * sum)

#5
def integration_simpson(a,b,n,l):
    if n % 2 != 0:
        print("n doit être pair")
        return 0
    h = (b - a) / n
    impair = 0
    for i in range(1,len(l) - 1,2):
        impair += l[i][1]
    pair = 0
    for j in range(2,len(l) - 1,2):
        pair += l[j][1]
    f_xo = l[0][1]
    f_xn = l[len(l) - 1][1]
    return (h / 3) * (f_xo + f_xn + (4 * impair) + (2 * pair))

#TO DO question 7

def main():
    #plot_function(x**3 + 1, -2, 2)
    #plot_fun_der(x**3 + 1,derive(x**3 + 1), -2, 2)
    #plot_fun_der_sec(x**3 + 1,derive(x**3 + 1),derive(derive(x**3 + 1)), -2, 2)
    #print(monotonie(x ** 2 + 1, 0.1, 2))
    #print(forme_courbe(x**2 + 1,-2,2))
    # print(lagrange(x**3+1,-2, 2))
    # plot_all(x**3 + 1,derive(x**3 + 1),derive(derive(x**3 + 1)), -2, 2)

    #exercice 9
    print("Exo 9")
    l = nuage_point(0,math.pi/2,4,lambda x: math.sin(x))
    print(l)
    approx_rect_inf = integration_rectange_inf(0, math.pi / 2, 4,l)
    print(approx_rect_inf)
    approx_rect_sup = integration_rectange_sup(0, math.pi / 2, 4,l)
    print(approx_rect_sup)
    approx_trapeze = integration_trapeze(0, math.pi / 2, 4,l)
    print(approx_trapeze)
    approx_simpson = integration_simpson(0, math.pi / 2, 4,l)
    print(approx_simpson)

    #exercie 10
    print("\nExo 10")
    l = [(0,30),(10,31.63),(20,33.44),(30,35.47),(40,37.75),(50,40.33),(60,43.29),(70,46.70),(80,50.67)]
    print(l)
    approx_rect_inf = integration_rectange_inf(0, 80, 8,l)
    print(approx_rect_inf)
    approx_rect_sup = integration_rectange_sup(0, 80, 8,l)
    print(approx_rect_sup)
    approx_trapeze = integration_trapeze(0, 80, 8,l)
    print(approx_trapeze)
    approx_simpson = integration_simpson(0, 80, 8,l)
    print(approx_simpson)

if __name__ == "__main__":
    main()