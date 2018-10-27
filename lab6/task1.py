import matplotlib.pyplot as plt
import numpy as np
from math import tan


def nonuniform_ascending_order(a, b, n):
    """
    Numbers on [a, b] span in ascending order of difference between pairs

    :param a: start
    :param b: stop
    :param n: amount of items
    :return:
    """
    res = []
    for i in range(n):
        res.append(a + ((b - a)*i**2)/n**2)
    return np.array(res)


def nonuniform_descending_order(a, b, n):
    """
        Numbers on [a, b] span in descending order of difference between pairs

        :param a: start
        :param b: stop
        :param n: amount of items
        :return:
        """
    res = []
    for i in range(n):
        res.append(b-((b - a)*(n - i)**2)/n**2)
    return np.array(res)


def integrate(func, xarr):
    """
    Integrates func, approximates area with rectangles

    :param func: callable func e.g. sin(x)/x
    :param a: lower bound
    :param b: upper bound
    :return: real value
    """
    total = 0
    for i in range(len(xarr)-1):
        total += func(xarr[i]) * abs(xarr[i+1] - xarr[i])
    return total


def task1(err, n):
    f = lambda x: np.exp(-x**2)
    A = np.log(1/err)
    print(A)
    xarr1 = np.linspace(0, A, n)
    xarr2 = nonuniform_ascending_order(0, A, n)
    xarr3 = nonuniform_descending_order(0, A, n)
    res1, res2, res3 = integrate(f, xarr1), integrate(f, xarr2), integrate(f, xarr3)
    return res1, res2, res3
"""
20.72326583694641
(0.8965989303761542, 0.8903600323345142, 0.9064939366212098)

20.72326583694641
(0.8863305428180974, 0.8862681881347884, 0.8864296639393391)
"""


def task2(err, n):
    f = lambda x: np.sin(x)/(x**2 + 1)
    A = tan(np.pi/2 - err)
    print(A)
    xarr1 = np.linspace(0, A, n)
    xarr2 = nonuniform_ascending_order(0, A, n)
    xarr3 = nonuniform_descending_order(0, A, n)
    res1, res2, res3 = integrate(f, xarr1), integrate(f, xarr2), integrate(f, xarr3)
    return res1, res2, res3
"""
99.99666664444354
(0.64584282542316, 0.6503983443213224, 0.6430048618630847)

99.99666664444354
(0.6466760738462318, 0.6467133186686425, 0.6466725586847585)
"""


def task3(err, n):
    f = lambda x: np.sin(x) / (1 - x)**0.5
    A = 1 - (err / 2) ** 2
    print(A)
    xarr1 = np.linspace(0, A, n)
    xarr2 = nonuniform_ascending_order(0, A, n)
    xarr3 = nonuniform_descending_order(0, A, n)
    res1, res2, res3 = integrate(f, xarr1), integrate(f, xarr2), integrate(f, xarr3)
    return res1, res2, res3
"""
0.99999975
(1.1481002775345235, 1.0951462375241452, 1.1792472641917375)

0.99999975
(1.183012407322545, 1.1776949733676716, 1.1860766344635423)

"""


def task4(err, n):
    f = lambda x: np.sin(x) / x
    A = 1/err
    xarr1 = np.linspace(err, A, n)      # from eps to A, not from 0 to A because of zero-division error
    xarr2 = nonuniform_ascending_order(err, A, n)
    xarr3 = nonuniform_descending_order(err, A, n)
    res1, res2, res3 = integrate(f, xarr1), integrate(f, xarr2), integrate(f, xarr3)
    return res1, res2, res3
"""
(1.5697327085758257, 1.5692702639149654, 1.5702323302594017)
1.5707963267948966


"""


if __name__ == '__main__':
    print(task4(10**-3, 10**8))
    print(np.pi/2)




 



