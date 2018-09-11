import numpy as np
import numpy.polynomial.polynomial as poly
from numpy.polynomial.polynomial import Polynomial


def lagr_poly(xlist, ylist):
    """
    Implements Lagrange's interpolation polynomial with values y[i] at points x[i] i = 1, n

    :param xlist: iterable with func argument
    :param ylist: iterable with func value
    :return: np Polynomial object
    """
    assert len(xlist) == len(ylist)
    assert len(set(xlist)) == len(xlist)
    poly_lst = []
    for i, xi in enumerate(xlist):
        l_i = Polynomial((1))       # unit polynomial, which will result in a Lagrange basis polynomial
        for xj in xlist:
            if xj != xi:
                l_i *= Polynomial((-xj / (xi - xj), 1 / (xi - xj))) # basis polynomial factor
        l_i *= ylist[i]
        poly_lst.append(l_i)
    return sum(poly_lst)


def integrate(func, a, b, k):
    """
    Calculates approximate value of definite integral on [a, b] span
    Based on idea of Simpson's approximation formula method interpolates function of [a, b] span with
    polynomial of k-1 degree

    :param func: math func {e.g. sin(x) + exp(x) - log^2(x)}
    :param a: lower bound
    :param b: upper bound
    :param k: degree of approx polynomial
    :return: real value
    """
    total = 0
    const = int(abs(b - a) / 0.1 + 1)
    xlist = np.linspace(a, b, const)
    # ylist = np.array([func(x) for x in xlist])
    for i in range(const-1):
        tmp_x_lst = np.linspace(xlist[i], xlist[i+1], k)
        tmp_y_lst = np.array([func(x) for x in tmp_x_lst])
        p = lagr_poly(tmp_x_lst, tmp_y_lst)
        pcoef = poly.polyint(p.coef)
        res = poly.polyval(xlist[i+1], pcoef) - poly.polyval(xlist[i], pcoef)
        total += res
    return np.round(total, 50)


if __name__ == '__main__':
    f1 = lambda x: np.sin(x) + x
    # f2 = lambda x: np.exp(-2*x) + x**2
    # f3 = lambda x: np.cos(x) + np.log(x+10)
    # for f in (f1, f2, f3):
    print(integrate(f1, -20, 20, 10))
