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


def test_error(err):
    """
    Searches for first point where error of differential of func is more than 0.1
    """
    f = lambda x1, x2, x3: np.exp(x1 + x2 + x3)
    x0 = (0, 0, 0)
    dx = 0.1
    maximum = -np.inf
    while True:
        # val = 0
        x = tuple([c+dx for c in x0])
        domain = [(x0[0]+i, x0[1]+i, x0[2]+i) for i in np.linspace(x0[0], x[0], 10)]
        for t in domain:
            if maximum > err:
                # compare(f, t)
                return t
            deriv_t = [part_diff(f, t, i) for i in range(len(t))]   # all partial derivatives at point t as vector
            deriv_x = [part_diff(f, x, i) for i in range(len(x))]   # all partial derivatives at point x as vector
            right_fact = sum([i**2 for i in (np.array(x) - np.array(x0))])*(1/2)    # right factor of formula
            val = (np.matrix(deriv_t) * np.matrix(deriv_x).transpose()) * right_fact # total value
            if val >= maximum:
                maximum = val
        dx += dx


def test2(x0):
    x00 = (0, 0, 0)
    # x0 = (1, 0.05, -0.01)
    f = lambda x1, x2, x3: np.exp(x1 + x2 + x3)
    deriv = []
    for i, arg in enumerate(x0):
        deriv.append(part_diff(f, x0, i))
    dx = list(np.array(x0) - np.array(x00))
    res = f(*x00) + np.matrix(deriv) * np.matrix(dx).transpose()
    return res