import matplotlib.pyplot as plt
import numpy as np
from sympy import *
import math

x = Symbol('x')
pas = 0.1

#Méthode pour obtenir la dérivé d'une fonction et l'évaluer
def d(f):return diff(f, x, 1)
def d2(f):return diff(f, x, 2)
def eval(f, t):return f.subs(x, t)

def tracer(f, start, end):
    X = np.arange(start, end + pas, pas)
    Y = [ eval(f, x) for x in X ]
    plt.title("Function " + str(f))
    plt.plot(X, Y)
    plt.axhline(0, color = "black")
    plt.axvline(0, color = "black")
    plt.grid()
    plt.show()

def monotonie(f, start, end):
    """Retourne 1 si croissant, -1 si décroissant, 0 sinon"""
    tab = np.arange(start, end, pas) # [start, start + pas, ..., end]
    derivee = [eval(d(f), t) for t in tab]
    croissant = [element > 0 for element in derivee]
    if all(croissant): #Tous les éléments de croissants est True
        return 1
    elif not any(croissant): #Tous les éléments de croissants est True
        return -1
    return 0

def convexite(f, start, end):
    """Retourne 1 si convexe, -1 si concave, 0 sinon"""
    return monotonie(d2(f), start, end)

def lagrange(f, start, end, erreur):
    if convexite(f, start, end) == 0:
        print("La fonction n'est ni concave ni convexe sur l'intervalle donné !")
        return 0
    if eval(f, start) * eval(d(f), start) > 0:
        pt_fixe, pt_pivot = start, end
    else:
        pt_fixe, pt_pivot = end, start
    x0 = pt_pivot
    xn = x0 - eval(f, x0) * (x0 - pt_fixe) / (eval(f, x0) - eval(f, pt_fixe))
    precision = [x0, xn]
    while abs(x0 - xn) > erreur:
        x0 = xn
        xn = xn - eval(f, xn) * (xn - pt_fixe) / (eval(f, xn) - eval(f, pt_fixe))
        precision.append(xn)
    return pt_fixe, precision


def newton(f, start, end, erreur):
    if convexite(f, start, end) == 0:
        print("La fonction n'est ni concave ni convexe sur l'intervalle donné !")
        return 0
    if eval(f, start) * eval(d(f), start) > 0:
        pt_fixe = star
    else:
        pt_fixe = end
    x0 = pt_fixe
    xn = x0 - eval(f, x0) / eval(d(f), x0)
    precision = [x0, xn]
    while abs(x0 - xn) > erreur:
        x0 = xn
        xn = xn - eval(f, xn) / eval(d(f), xn)
        precision.append(xn)
    return pt_fixe, precision
    
def tracer_corde_lagrange(f, start, end, cordes):
    X = np.arange(start, end + pas, pas)
    Y = [ eval(f, x) for x in X ]
    plt.title("Function " + str(f) + " avec méthode de Lagrange")
    plt.plot(X, Y)

    pt_fixe, precision = cordes
    taille_max = 5 if len(precision) > 5 else len(precision)
    for c in precision[:taille_max]:
        plt.plot([c, pt_fixe], [eval(f, c), eval(f, pt_fixe)], color='r', linestyle=':')

    plt.axhline(0, color = "black")
    plt.axvline(0, color = "black")
    plt.grid()
    plt.show()

def tracer_corde_newton(f, start, end, cordes):
    X = np.arange(start, end + pas, pas)
    Y = [ eval(f, x) for x in X ]
    plt.title("Function " + str(f) + " avec méthode de Lagrange")
    plt.plot(X, Y)

    pt_fixe, precision = cordes
    taille_max = 5 if len(precision) > 5 else len(precision)
    for i in range(1, taille_max):
        c = precision[i]
        avant = precision[i - 1]
        plt.plot([c, c], [0, eval(f, c)], color='black', linestyle='--')
        plt.plot([c, avant], [0, eval(f, avant)], color='r', linestyle=':')

    plt.axhline(0, color = "black")
    plt.axvline(0, color = "black")
    plt.grid()
    plt.show()

def ex(f, start, end, erreur):
    print(f)
    tracer(f, -1, 2)

    pt_f_L, precision_L  = lagrange(f, start, end, erreur)
    pt_f_N, precision_N  = newton(f, start, end, erreur)

    tracer_corde_lagrange(f, start, end, (pt_f_L, precision_L))
    tracer_corde_newton(f, start, end, (pt_f_N, precision_N))

    
f1 = x**3 + x - 1
f2 = x - exp(-x)

ex(f1, 0, 2, 0.01)
ex(f2, 0, 1, 0.01)