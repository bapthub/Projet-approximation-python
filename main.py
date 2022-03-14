import matplotlib.pyplot as plt
import numpy as np
from sympy import *

x = Symbol('x')

#def f(x):
    #return x**3 + 1

y = x**3 + 1

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
    return 0

def main():
    #plot_function(x**3 + 1, -2, 2)
    #plot_fun_der(x**3 + 1,derive(x**3 + 1), -2, 2)
    #plot_fun_der_sec(x**3 + 1,derive(x**3 + 1),derive(derive(x**3 + 1)), -2, 2)
    plot_all(x**3 + 1,derive(x**3 + 1),derive(derive(x**3 + 1)), -2, 2)

if __name__ == "__main__":
    main()