import numpy as np
from math import log


def part_diff(f, x0: tuple, argnum):
    """
    Partial derivative of func f at point x0 by argnumth's argument
    f(x, y), x0 = (1, 1), argnum = 1 will find df(x0)/dy
    """
    dx = 10**-5
    upper = f(*x0[:argnum], x0[argnum]+dx, *x0[argnum+1:]) - f(*x0)
    lower = dx
    return upper/lower


def test1():
    x0 = (1, 0)
    xarr = [(1.5, 0.7), (1.05, 0.07), (1.005, 0.007)]
    f = lambda x1, x2: x1 ** 5 * log(1 + x2 ** 2)
    for x in xarr:
        deriv = []
        for i, arg in enumerate(x):
            deriv.append(part_diff(f, x, i))
        dx = list(np.array(x) - np.array(x0))
        res = f(*x0) + np.matrix(deriv) * np.matrix(dx).transpose()
        print(res)