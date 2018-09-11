import numpy as np


def log_zeroes(f, a, b):
    print(f(a), f(b))
    try:
        assert f(a) * f(b) < 0
    except AssertionError:
        raise Exception('Incorrect function: values on the edges are supposed to have different signs')
    eps = 10**(-6)
    if abs(f(a)) < eps:
        return a
    elif abs(f(b)) < eps:
        return b
    else:
        c = (a + b)/2
        if f(c) * f(a) < 0:
            return log_zeroes(f, a, c)
        elif f(c) * f(b) < 0:
            return log_zeroes(f, c, b)


def der(f, x0):
    dx = 10**(-10)
    tmp1 = f(x0+dx) - f(x0-dx)
    tmp2 = 2*dx
    return tmp1/tmp2


def tangent_zeroes(f, x0):
    """"""
    # print(x0, f(x0))
    eps = 10**(-6)
    if abs(f(x0)) < eps:
        return x0
    else:
        x0 = x0 - f(x0)/der(f, x0)
        return tangent_zeroes(f, x0)


def secant_zeroes(f, a, b):
    """"""
    eps = 10**(-6)
    x0 = a
    x1 = b
    if abs(f(x0)) < eps:
        return x0
    elif abs(f(x1)) < eps:
        return x1
    else:
        x1 = x1 - f(x1)*(x1-x0)/(f(x1)-f(x0))
        x0 = b
        return secant_zeroes(f, x0, x1)


if __name__ == '__main__':
    f1 = lambda x: x**10 - 0.1*x - 0.01
    f2 = lambda x: 6*np.sin(x**7) + x**21 - 6*x**14
    f3 = lambda x: np.log(x) + np.sin(x)

    #  f1
    #  0.7846527099609375
    # -0.09999999899960554
    # -0.10000000000000428

    #  f2
    # 0.09999999999999998
    # 0.09253257934657529
    # -0.0985647217146712

    #   f3
    # 0.5787137985229491
    # 0.5787136376113005
    # 0.5787136436252428


    print(log_zeroes(f2, -0.4, 0.6))
    print(tangent_zeroes(f2, 0.2))
    print(secant_zeroes(f2, -0.4, 0.6))