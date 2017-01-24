'''
Uncertainty Calculator:
using general formula
a = partial deriv symbol
R is the result
r is the uncertainty of result
R= R(X,Y,Z,...) -> e.g. R = X * Y - Z
r = sqrt( (ar/ax * x)**2 + (ar/ay * y)**2 
'''

from sympy import *
x, y, z = symbols('x y z')
init_printing(use_unicode=True)
print('a')
print(diff(cos(x), x))
