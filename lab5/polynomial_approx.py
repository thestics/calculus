import numpy as np
from numpy import linalg
import matplotlib.pyplot as plt


def build_a(xarr, deg):
    """
    Builds A matrix
    [
        [x0^0, x0^1, ... , x0^deg],
        [x1^0, x1^1, ... , x1^deg],
        ...
        [xn^0, xn^1, ... , xn^deg]
    ]

    :param xarr: [x0, x1, ..., xn]
    :param deg:  degree of polynomial
    :return: matrix A
    """
    A = []
    for x in xarr:
        row = []
        for n in range(deg + 1):
            row.append(x**n)
        A.append(row)
    return np.matrix(A)


def tabulate(f, xarr):
    """
    For a domain and function, builds a values array

    :param f:
    :param xarr:
    :return:
    """
    return [f(x) for x in xarr]


def plot_by_coefficients(coefs, func, a, b):
    """
    Plots func and polynomial with coeffcients "coefs" on [a, b] span on same canvas

    :param coefs: coefficients list
    :param func: callable
    :param a:
    :param b:
    :return:
    """
    f = lambda x: sum([coefs[i]*x**i for i in range(len(coefs))])
    domain = np.linspace(a, b, 100)
    y1 = [f(x) for x in domain]
    y2 = [func(x) for x in domain]
    plt.plot(domain, y1)
    plt.plot(domain, y2, '.')
    plt.show()


def task1(f, a, b, m, n):
    xarr = np.linspace(a, b, n+1)
    B = np.matrix(tabulate(f, xarr)).transpose()
    A = build_a(xarr, m)
    left = A.transpose()*A
    print(left)
    right = A.transpose()*B
    print(right)
    res = linalg.solve(left, right)
    coefs = list(res.flat)
    plot_by_coefficients(coefs, f, a, b)
    return res



if __name__ == '__main__':
    f1 = lambda x: np.sin(x)
    f2 = lambda x: np.exp(x)
    a = 0
    b = 4*np.pi
    m = 10
    n = 10
    print(task1(f1, a, b, m, n))
















