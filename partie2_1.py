import matplotlib.pyplot as plt
import numpy as np
import scipy as sci
import sympy as sym
from scipy.optimize import minimize_scalar
from sympy.plotting import plot
from numpy.linalg import inv
from sympy import *
import math

plt.style.use('seaborn-poster')
# %matplotlib inline

x = Symbol('x')

#3
def vander_method(l_x,l_y):
    m = np.zeros((len(l_x),len(l_x)),dtype=int)
    for i in range(len(m)):
        for j in range(len(m[i])):
            if i == 0:
                m[i][j] = l_x[i]
            else:
                m[i][j] = l_x[i]**j
    inv_matrix_v = inv(m)
    coeff = inv_matrix_v @ l_y
    # for i in range(len(coeff)):
    #     coeff[i] = round(coeff[i],3)
    return coeff

#5
def divided_diff(x, y):
    n = len(y)
    coef = np.zeros([n, n])
    # the first column is y
    coef[:,0] = y

    for j in range(1,n):
        for i in range(n-j):
            coef[i][j] = \
           (coef[i+1][j-1] - coef[i][j-1]) / (x[i+j]-x[i])
    #round to 3 digits
    # for i in range(len(coef)):
    #     coef[i] = np.round(coef[i],3)
    return coef

def calculatate_prod(l_x,i,j):
    current_x = l_x[i]
    res = 1
    for k in range(j):
        res *= current_x - l_x[k]
    return res

# l = [1,2,4,6,7]
# print(calculatate_prod(l,4,4))

def newton_method(l_x,l_y):
    m = np.zeros((len(l_x),len(l_x)),dtype=int)
    for i in range(len(m)):
        for j in range(len(m)):
            if j == 0:
                m[i][j] = 1
            else:
                m[i][j] = calculatate_prod(l_x,i,j)
    inv_matrix_v = inv(m)
    coeff = inv_matrix_v @ l_y
    # round to 3 digits
    # for i in range(len(coeff)):
    #     coeff[i] = round(coeff[i],3)
    return coeff

# def newton_poly(coef, x_data, x):
#     '''
#     evaluate the newton polynomial at x
#     '''
#     n = len(x_data) - 1
#     p = coef[n]
#     for k in range(1,n+1):
#         p = coef[n-k] + (x -x_data[n-k])*p
#     return p

#exo 5
# x = np.array([1, 2, 3, 4])
# y = np.array([1, 8, 27, 64])
# # difference divisée
# coeff = divided_diff(x, y)[0, :]
# (x1,x2,x3) = ("(x - " + str(x[0]) + ")","(x - " + str(x[1]) + ")","(x - " + str(x[2]) + ")")
# (a,b,c,d) = (str(int(coeff[0])),str(int(coeff[1])),str(int(coeff[2])),str(int(coeff[3])))
# pol = a + " + " + b + x1 + " + " + c + x1 + x2 + " + " + d + x1 + x2 + x3
# print(pol)

# lower_limit = 0
# upper_limit = 4.5
# num_pts = 100
# coeff = [1,0,0,0]
# x_line = np.linspace(lower_limit, upper_limit, num_pts)
# print(x_line)
# y_new = np.polyval(coeff, x_line)
# plt.figure(figsize = (10, 6))
# plt.plot(x, y, 'bo')
# plt.plot(x_line, y_new, '-b')
# plt.show()

#bad print
# evaluer d'autres points
# x_new = np.arange(-5, 2.1, .1)
# y_new = newton_poly(coeff, x, x)
# plt.figure(figsize = (10, 6))
# plt.plot(x, y, 'bo')
# plt.plot(x, y_new)
# plt.show()

# #exo 6
print("\nExercice 6:\nInterpolation de Newton")
x = np.array([1, 2, 4, 6, 7])
y = np.array([1, 3, -1, 5, 0])
# difference divisée
coeff = divided_diff(x, y)[0, :]
(x1,x2,x3,x4) = ("(x - " + str(x[0]) + ")","(x - " + str(x[1]) + ")","(x - " + str(x[2]) + ")","(x - " + str(x[3]) + ")")
(a,b,c,d,e) = (str(coeff[0]),str(coeff[1]),str(coeff[2]),str(coeff[3]),str(coeff[4]))
pol = a + " + " + b + x1 + " + " + c + x1 + x2 + " + " + d + x1 + x2 + x3 + " + " + e + x1 + x2 + x3 + x4
print("Polynome difference divisée : ",pol)

#matrice triangulaire
coeff = newton_method(x,y)
(a,b,c,d,e) = (str(coeff[0]),str(coeff[1]),str(coeff[2]),str(coeff[3]),str(coeff[4]))
pol = a + " + " + b + x1 + " + " + c + x1 + x2 + " + " + d + x1 + x2 + x3 + " + " + e + x1 + x2 + x3 + x4
print("Polynome matrice triangulaire : ",pol)

#plot
lower_limit = 0
upper_limit = 8
num_pts = 100
coeffs = [(-13/60),10/3,-205/12,199/6,-91/5]
coeffs_round = [(-13/60),10/3,-205/12,199/6,-91/5]
for i in range(len(coeffs_round)):
        coeffs_round[i] = round(coeffs_round[i],3)
print("Polynome réduit : ",str(coeffs[0]) + " x^4" + " + " + str(coeffs[1]) + " x^3 " + str(coeffs[2]) + " x^2" + " + " + str(coeffs[3]) + " x " + str(coeffs[4]))
print("Polynome réduit arondi: ",str(coeffs_round[0]) + " x^4" + " + " + str(coeffs_round[1]) + " x^3 " + str(coeffs_round[2]) + " x^2" + " + " + str(coeffs_round[3]) + " x " + str(coeffs_round[4]))
x_line = np.linspace(lower_limit, upper_limit, num_pts)
y_new = np.polyval(coeffs, x_line)
plt.figure(figsize = (10, 6))
plt.plot(x, y, 'bo')
plt.plot(x_line, y_new, '-b')

coeff = vander_method(x,y)
for i in range(len(coeffs_round)):
        coeffs_round[i] = round(coeffs_round[i],3)
print("\nInterpolation de Vandermonde :")
print("Polynome matrice de Vandermonde :",str(coeff[4]) + " x^4" + " + " + str(coeff[3]) + " x^3 " + str(coeff[2]) + " x^2" + " + " + str(coeff[1]) + " x " + str(coeff[0]))
#plot
poly_coefs = coeff[::-1]
x_line = np.linspace(lower_limit, upper_limit, num_pts)
y_new = np.polyval(poly_coefs, x_line)
plt.figure(figsize = (10, 6))
plt.plot(x, y, 'bo')
plt.plot(x_line, y_new, '-b')

plt.show()

#vandermonde
#exo 5
# x = np.array([1, 2, 3, 4])
# y = np.array([1, 8, 27, 64])
# coeff = vander_method(x,y)
# print(str(int(coeff[3])) + " x^3 " + " + "  + str(coeff[2]) + " x^2 " + str(coeff[1]) + " x " + " + " + str(coeff[0]))
# #plot
# lower_limit = 0
# upper_limit = 8
# num_pts = 100
# poly_coefs = coeff[::-1]
# x_line = np.linspace(lower_limit, upper_limit, num_pts)
# y_new = np.polyval(poly_coefs, x_line)
# plt.figure(figsize = (10, 6))
# plt.plot(x, y, 'bo')
# plt.plot(x_line, y_new, '-b')
# plt.show()

#exo 6
#vandermonde
# x = np.array([1, 2, 4, 6, 7])
# y = np.array([1, 3, -1, 5, 0])
# coeff = vander_method(x,y)
# print(str(coeff[4]) + " x^4" + " + " + str(coeff[3]) + " x^3 " + str(coeff[2]) + " x^2" + " + " + str(coeff[1]) + " x " + str(coeff[0]))
# #plot
# lower_limit = 0
# upper_limit = 8
# num_pts = 100
# poly_coefs = coeff[::-1]
# x_line = np.linspace(lower_limit, upper_limit, num_pts)
# y_new = np.polyval(poly_coefs, x_line)
# plt.figure(figsize = (10, 6))
# plt.plot(x, y, 'bo')
# plt.plot(x_line, y_new, '-b')
# plt.show()
