
import matplotlib.pyplot as plt
import numpy as np
from numpy import matrix
import random
from math import log


def test1(x0):
    f = lambda x: 0.5 * np.cos(x)
    x1 = f(x0)
    lmbd = 0.5
    count = int(log((10**-9*(1-lmbd))/abs(x1-x0), lmbd) + 1)
    for i in range(count):
        x0 = x1
        x1 = f(x0)
    return x1


def test2(x0):
    lmbd = 1/(2**5*5 - 2)
    f = lambda x: x - lmbd*(x**5 - x - 1)
    x1 = f(x0)
    L = 1 - 1/4
    count = int(log((10**-9*(1-L))/abs(x1-x0), L) + 1)
    # print(count)
    for i in range(count):
        x0 = x1
        x1 = f(x0)
    return x1


def test3(c, b):
    """

    :param a:   matrix ([[1,2,3],[4,5,6],[0,5,7]])
    :param b:   column-vector ([[1],[2],[3]])
    :return:
    """
    C = matrix(c)
    b = matrix(b)
    x0 = matrix([[1] for i in range(len(C))])   # start vector
    lmbd = float(sum(C.getA1()**2)**(1/2))
    eye = matrix(np.eye(len(C)))
    if lmbd < 1:
        f = lambda x: (C+eye)*x + b - x
        x1 = f(x0)
        m = sum([(vi - gi)**2 for vi in b.flat for gi in x0.flat])**(1/2)
        count = int(log((10 ** - 9 * (1 - lmbd)) / m, lmbd) + 1)
        for i in range(count):
            x1 = f(x1)
        print(f'A*x:{(C+eye)*x1}', end='\n')
        print(f'b:{b}', end='\n\n\n')
        return x1
    else:
        return


def exponential_metrics(f, g, k, domain):
    max = -np.inf
    for i in range(len(domain)):
        x = domain[i]
        term = np.exp(-k*(x-domain[0])) * abs(f(x) - g(x))
        if term >= max:
            max = term
    return max


def integral_trapezoid(func, j, xarr):
    """
    Integrates func, approximates area with trapezoids

    :param func: callable func e.g. sin(x)/x
    :param a: lower bound
    :param b: upper bound
    :return: real value
    """
    # const = int(abs(b - a)/0.1 + 1)
    # xarr = np.linspace(a, b, n)
    total = 0
    for i in range(len(xarr) - 1):
        total += (func(xarr[i]) + func(xarr[i+1]))/2 * abs(xarr[i+1] - xarr[i])
        if i >= j:
            break
    return total


def _build_y1(x0, y0, a, b, n):
    xarr = np.linspace(a, b, n)
    y = lambda x: x - x0 + y0
    func = lambda x: 0.5 * np.arctan(y(x)) + x ** 5
    funcarr = []
    for i in range(len(xarr)):
        val = y0 + integral_trapezoid(func, i, xarr)
        funcarr.append(val)
    data = dict(zip(xarr, funcarr))
    return lambda x: data[x]



def test4(x0, y0, a, b, n):
    L = 0.4                         # L >= pi/8
    k = 0.8                         # k > L
    lmbd = L/k
    xarr = np.linspace(a, b, n)
    y = lambda x: x - x0 + y0       # linear start func which contain point (x0, y0)
    y1 = _build_y1(x0, y0, a, b, n)
    d = exponential_metrics(y, y1, k, xarr)
    count = int(log((10 ** - 9 * (1 - lmbd)) / d, lmbd) + 1)
    func = lambda x: 0.5 * np.arctan(y(x)) + x ** 5
    # count = 5                       # pre-value
    for i in range(count):
        funcarr = []
        for j in range(len(xarr)):
            val = y0 + integral_trapezoid(func, j, xarr)
            funcarr.append(val)
        plt.plot(xarr, np.array(funcarr))
        data = dict(zip(xarr, funcarr))
        y = lambda x: data[x]
        func = lambda x: 0.5 * np.arctan(y(x)) + x ** 5
    plt.show()



if __name__ == '__main__':
    print(f'test 1: {test1(0)}')
    print(f'test 2: {test2(1.5)}')

    a = [[random.random()/10 - 0.05 for i in range(10)] for j in range(10)]
    b = [[random.random()*20 - 10] for i in range(10)]
    # print(f'test 3.1: {test3(a, b)}')
    test3(a, b)
    a = [[random.random()/50 - 0.01 for i in range(80)] for j in range(80)]
    b = [[random.random()*20 - 10] for i in range(80)]
    test3(a, b)
    test4(0, 2, 0, 2, 200)