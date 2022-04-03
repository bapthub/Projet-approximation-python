import matplotlib.pyplot as plt
import numpy as np
from sympy import *
from scipy.optimize import fsolve

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
    tab = np.arange(start, end + pas, pas) # [start, start + pas, ..., end]
    derivee = [eval(d(f), t) for t in tab if eval(d(f), t).is_real]
    croissant = [element >= 0 for element in derivee]
    if all(croissant): #Tous les éléments de croissants est True
        return 1
    elif not any(croissant): #Tous les éléments de croissants est True
        return -1
    return 0

def convexite(f, start, end):
    """Retourne 1 si convexe, -1 si concave, 0 sinon"""
    return monotonie(d(f), start, end)

def lagrange(f, start, end, erreur):
    if convexite(f, start, end) == 0:
        print("La fonction n'est ni concave ni convexe sur l'intervalle donné !")
        return 0, []
    if eval(f, start) * eval(d2(f), start) > 0:
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
        return 0, []
    if eval(f, start) * eval(d(f), start) > 0:
        pt_fixe = start
    else:
        pt_fixe = end
    x0 = pt_fixe
    xn = x0 - eval(f, x0) / eval(d(f), x0)
    precision = [x0, xn]
    while abs(x0 - xn) > erreur:
        x0 = xn
        xn = xn - eval(f, xn) / eval(d(f), xn)
        precision.append(xn)
    return x0, precision
    
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
    plt.title("Function " + str(f) + " avec méthode de Newton")
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
    print("Fonction :", f)
    print("Solution :", [item.evalf() for item in solve(f, x) if item.is_real])
    tracer(f, start, end)

    pt_f_L, precision_L  = lagrange(f, start, end, erreur)
    pt_f_N, precision_N  = newton(f, start, end, erreur)

    print("Precision Lagrange : ", [float(item) for item in precision_L])
    print("Precision Newton : ", [float(item) for item in precision_N])

    tracer_corde_lagrange(f, start, end, (pt_f_L, precision_L))
    tracer_corde_newton(f, start, end, (pt_f_N, precision_N))
    print()

f1 = x**3 + x - 1
f2 = x - exp(-x)
f3 = 1 - x**2

ex(f1, 0, 2, 0.01)
ex(f2, 0, 1, 0.01)
ex(f3, 0, 2, 0.01)

def monotonie_intervalle(f, start, end):
    """Retourne une liste d'intervalle croissant ou décroissant"""
    croissant = []
    decroissant = []
    tab = np.arange(start, end + pas, pas)
    derivee = [eval(d(f), t) for t in tab if eval(d(f), t).is_real]
    check = [element >= 0 for element in derivee]
    i = 0
    while i < len(derivee):
        croiss = []
        decroiss = []
        while i < len(check) and check[i]:
            if (len(croiss) == 0):
                croiss.append(tab[i])
            i += 1
        if (len(croiss) == 1):
            croiss.append(tab[i - 1])
        
        while i < len(check) and not check[i]:
            if (len(decroiss) == 0):
                decroiss.append(tab[i])
            i += 1
        if (len(decroiss) == 1):
            decroiss.append(tab[i - 1])
        if len(decroiss) == 2:
            decroissant.append(decroiss)
        if len(croiss) == 2:
            croissant.append(croiss)
        i += 1
    return croissant, decroissant

def convexite_intervalle(f, start, end):
    """Retourne une liste d'intervalle convexe ou concave"""
    return monotonie_intervalle(d(f), start, end)

def onlyNewton(f, start, end, erreur):
    print("Fonction :", f)
    print("Solution :", [item.evalf() for item in solve(f, x) if item.is_real])
    tracer(f, start, end)

    pt_f_N, precision_N  = newton(f, start, end, erreur)

    print("Precision Newton : ", [float(item) for item in precision_N])
    tracer_corde_newton(f, start, end, (pt_f_N, precision_N))
    print()

f4 = x**3 - 2 * x + 3

print(monotonie_intervalle(f4, -50, 50))
print(convexite_intervalle(f4, -50, 50))
onlyNewton(f4, -10, -1, 0.1)