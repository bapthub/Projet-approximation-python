import matplotlib.pyplot as plt
import numpy as np
import scipy as sci
import sympy as sym
from scipy.optimize import minimize_scalar
from sympy import *
import math

x = Symbol('x')
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

#7
def n_derivative(f,n):
    return diff(f,x,n)

def find_max(f,a,b):
    res_max = sci.optimize.minimize_scalar(f, bounds=[a,b], method='bounded')
    return (res_max.x,-res_max.fun)

def find_min(f,a,b):
    res_min = sci.optimize.minimize_scalar(f, bounds=[a,b], method='bounded')
    return (res_min.x,-res_min.fun)

def nb_div_rectangle(a,b,c,e):
    num = (b-a)**2 * c
    den = 2 * e
    res = (num / den)
    res = int(math.ceil(res))
    return res

def nb_div_trapeze(a,b,c,e):
    num = (b-a)**3 * c
    den = 12 * e
    res = (num / den)**0.5
    res = int(math.ceil(res))
    return res

def nb_div_simpson(a,b,c,e):
    num = (b-a)**5 * c
    den = 180 * e
    res = (num / den)**0.25
    res = int(math.ceil(res))
    if res % 2 == 1:
        return res + 1
    return res


def main():
    #exercice 9
    print("Exo 9")
    l = nuage_point(0,math.pi/2,4,lambda x: math.sin(x))
    print(l)
    approx_rect_inf = integration_rectange_inf(0, math.pi / 2, 4,l)
    print("approx_rect_inf I = ",approx_rect_inf)
    approx_rect_sup = integration_rectange_sup(0, math.pi / 2, 4,l)
    print("approx_rect_sup I = ",approx_rect_sup)
    approx_trapeze = integration_trapeze(0, math.pi / 2, 4,l)
    print("approx_trapeze I = ",approx_trapeze)
    approx_simpson = integration_simpson(0, math.pi / 2, 4,l)
    print("approx_simpson I = ",approx_simpson)

    #exercie 10
    print("\nExo 10")
    l = [(0,30),(10,31.63),(20,33.44),(30,35.47),(40,37.75),(50,40.33),(60,43.29),(70,46.70),(80,50.67)]
    print(l)
    approx_rect_inf = integration_rectange_inf(0, 80, 8,l)
    print("approx_rect_inf I = ",approx_rect_inf)
    approx_rect_sup = integration_rectange_sup(0, 80, 8,l)
    print("approx_rect_sup I = ",approx_rect_sup)
    approx_trapeze = integration_trapeze(0, 80, 8,l)
    print("approx_trapeze I = ",approx_trapeze)
    approx_simpson = integration_simpson(0, 80, 8,l)
    print("approx_simpson I = ",approx_simpson)

    #rectangle
    print("\nf(x) = sin(1/x)")
    print("Rectangle :")
    #utiliser sym
    def f(x):
        return sym.sin(1/x)
    print("dérivée :",diff(f(x),x,1))
    #defnir a et b bornes
    (a,b) = (1,10)
    #utiliser math
    # derivée nième normale
    def deriv_f(x):
        return -math.cos(1/x)/x**2
    # derivée nième avec le signe -
    def deriv_f_contraire(x):
        return math.cos(1/x)/x**2
    #get the max in the interval
    (x_max,max_val) = find_max(deriv_f_contraire,a,b)
    (x_min,min_val) = find_min(deriv_f,a,b)
    max_val = max(abs(max_val),abs(min_val))
    print("val max sur I:",max_val)
    #final
    print("n=:",nb_div_trapeze(a,b,max_val,10**-7))

    #trapeze
    print("\nTrapeze :")
    #utiliser sym
    def f(x):
        return sym.sin(1/x)
    print("dérivée seconde :",diff(f(x),x,2))
    #defnir a et b bornes
    (a,b) = (1,10)
    #utiliser math
    # derivée nième normale
    def deriv_f(x):
        return (2*math.cos(1/x) - math.sin(1/x)/x)/x**3
    # derivée nième avec le signe -
    def deriv_f_contraire(x):
        return -(2*math.cos(1/x) - math.sin(1/x)/x)/x**3
    #get the max in the interval
    (x_max,max_val) = find_max(deriv_f_contraire,a,b)
    (x_min,min_val) = find_min(deriv_f,a,b)
    max_val = max(abs(max_val),abs(min_val))
    print("val max sur I:",max_val)
    #final
    print("n=:",nb_div_trapeze(a,b,max_val,10**-7))

    #simpson
    print("\nSimpson :")
    (a,b) = (1,10)
    #definition fonction
    def f(x):
        return sym.sin(1/x)
    print("dérivée quatrième :", diff(f(x),x,4))
    #utiliser math
    #derivée nième normale
    def deriv_f(x):
        return (24*math.cos(1/x) - 36*math.sin(1/x)/x - 12*math.cos(1/x)/x**2 + math.sin(1/x)/x**3)/x**5
    #derivée nième avec le signe - devant
    def deriv_f_contraire(x):
        return -(24*math.cos(1/x) - 36*math.sin(1/x)/x - 12*math.cos(1/x)/x**2 + math.sin(1/x)/x**3)/x**5
    #get the max in the interval
    (x_max,max_val) = find_max(deriv_f_contraire,a,b)
    (x_min,min_val) = find_min(deriv_f,a,b)
    max_val = max(abs(max_val),abs(min_val))
    print("val max sur I:",max_val)
    #final
    print("n=",nb_div_simpson(a,b,max_val,10**-7))

    l = nuage_point(1,10,186,f)
    approx_simpson = integration_simpson(1, 10, 186,l)
    print("I ~= ",approx_simpson)

    #ex 12
    #trapeze
    #utiliser sym
    # def f(x):
    #     return x * sym.exp(-x)
    # print(diff(f(x),x,2))
    # #defnir a et b bornes
    # (a,b) = (0,1)
    # #utiliser math
    #derivée nième normale
    # def deriv_f(x):
    #     return -((x - 2) * math.exp(-x))
    # derivée nième avec le signe -
    # def deriv_f_contraire(x):
    #     return (x - 2) * math.exp(-x)
    # #get the max in the interval
    # (x_max,max_val) = find_max(deriv_f_contraire,a,b)
    # (x_min,min_val) = find_min(deriv_f,a,b)
    # max_val = max(abs(max_val),abs(min_val))
    # print(max_val)
    # #final
    # print(nb_div_trapeze(a,b,max_val,10**-8))

    #simpson
    # (a,b) = (0,1)
    # #definition fonction
    # def f(x):
    #     return x * sym.exp(-x)
    # print(diff(f(x),x,4))
    # #utiliser math
    # #derivée nième normale
    # def deriv_f(x):
    #     return -(x - 4)*math.exp(-x)
    # #derivée nième avec le signe - devant
    # def deriv_f_contraire(x):
    #     return (x - 4)*math.exp(-x)
    # #get the max in the interval
    # (x_max,max_val) = find_max(deriv_f_contraire,a,b)
    # (x_min,min_val) = find_min(deriv_f,a,b)
    # max_val = max(abs(max_val),abs(min_val))
    # print(max_val)
    # #final
    # print(nb_div_simpson(a,b,max_val,10**-8))

if __name__ == "__main__":
    main()
