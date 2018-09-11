import numpy as np
import numpy.random as rand


def integral_rectangle(func, a, b):
    """
    Integrates func, approximates area with rectangles

    :param func: callable func e.g. sin(x)/x
    :param a: lower bound
    :param b: upper bound
    :return: real value
    """
    const = int(abs(b - a)/0.01 + 1)
    xarr = np.linspace(a, b, const)
    total = 0
    for i in range(const - 1):
        total += func(xarr[i]) * abs(xarr[i+1] - xarr[i])
    return total


def integral_trapezoid(func, a, b):
    """
    Integrates func, approximates area with trapezoids

    :param func: callable func e.g. sin(x)/x
    :param a: lower bound
    :param b: upper bound
    :return: real value
    """
    const = int(abs(b - a)/0.01 + 1)
    xarr = np.linspace(a, b, const)
    total = 0
    for i in range(const - 1):
        total += (func(xarr[i]) + func(xarr[i+1]))/2 * abs(xarr[i+1] - xarr[i])
    return total


def integral_simpson(func, a, b):
    """
    Integrates func with simpson formula

    :param func: callable func e.g. sin(x)/x
    :param a: lower bound
    :param b: upper bound
    :return: real value
    """
    f = func
    const = int(abs(b - a) / 0.01 + 1)
    xarr = np.linspace(a, b, const)
    total = 0
    for i in range(const - 1):
        total += (f(xarr[i])/6 + 2/3 * f((xarr[i] + xarr[i+1])/2) + f(xarr[i+1])/6) * abs(xarr[i+1] - xarr[i])
    return total


def integral_monte_carlo(func, a, b):
    """
    Integrates func with monte-carlo method

    :param func: callable func e.g. sin(x)/x
    :param a: lower bound
    :param b: upper bound
    :return: real value
    """
    const = int(abs(b - a) / 0.0001 + 1)
    xarr = rand.random_sample(const)
    xarr *= abs(b-a)      # values shift in order to stay in [a, b] bounds
    xarr += a
    total = 0
    for i in range(const):
        total += func(xarr[i])
    return total/const * abs(b-a)


if __name__ == '__main__':
    # f = lambda x: np.sin(x) + x + x**3
    # print(integral_monte_carlo(f, -5, 5))
    f1 = lambda x: x + np.cos(x)
    f2 = lambda x: 3 ** (-x ** 2)
    f3 = lambda x: np.sin(x ** 10)
    f4 = lambda x: np.log(x)**(np.sin(2*x))**2
    f5 = lambda x: np.exp(-2*x**2 + np.cos(x))
    print(integral_trapezoid(f1, -50, 50))
    print(integral_trapezoid(f2, 0.9, 1))
    print(integral_trapezoid(f3, 0, 1))
    print(integral_trapezoid(f4, 1, 5))
    print(integral_trapezoid(f5, -2, 4))
