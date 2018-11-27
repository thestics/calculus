from int_methods_roots.main_int import integral_trapezoid
import numpy as np


def integral(func, xarr):
    """
    Integrates func, approximates area with rectangles
    Fragmentation of span [a, b] performed before, result -- :xarr:

    :param func: callable func e.g. lambda x: sin(x)/x
    :return: real value
    """
    total = 0
    for i in range(len(xarr)-1):
        total += func(xarr[i]) * abs(xarr[i+1] - xarr[i])
    return total


def build_integrate_func(f, curve_funcs, curve_func_derivs):
    """
    Builds subintegral function for line integral

    :param f:   func, defined on this line
    :param curve_funcs:     parametric deffinition of curve as a list of functions
    :param curve_func_derivs:   derivatives of each function
    """
    res = lambda t: f(*[f1(t) for f1 in curve_funcs]) * sum([f2(t)**2 for f2 in curve_func_derivs])**0.5
    return res


def curve_len(curve_funcs, curve_func_derivs, a, b):
    """
    Calculates length of curve defined parametrically, with functions :curve_funcs: on a,b span

    :param curve_funcs: parametric definition of curve
    :param curve_func_derivs: derivatives of curve_funcs
    """
    func = build_integrate_func(lambda *t: 1, curve_funcs, curve_func_derivs)
    len = integral_trapezoid(func, a, b)
    return len


def curve_mass(curve_funcs, curve_funcs_derivs, density_func, a, b):
    func = build_integrate_func(density_func, curve_funcs, curve_funcs_derivs)
    mass = integral_trapezoid(func, a, b)
    return mass


def curve_centre_of_mass(curve_func, curve_func_derivs, density_func, a, b):
    mass = curve_mass(curve_func, curve_func_derivs, density_func, a, b)
    func = build_integrate_func(density_func, curve_func, curve_func_derivs)
    xi = []
    for u in curve_func:
        f = lambda t: u(t) * func(t)
        xi.append(integral_trapezoid(f, a, b)/mass)
    return xi


def task1_1():
    curve_funcs = [lambda t: np.exp(t), lambda t: np.cos(t), lambda t: t**7]
    curve_funcs_derivs = [lambda t: np.exp(t), lambda t: -np.sin(t), lambda t: 7*t**6]
    len = curve_len(curve_funcs, curve_funcs_derivs, 0, 1)
    return len


def task1_2():
    curve_funcs = [lambda t: np.exp(t), lambda t: np.cos(t), lambda t: t ** 7]
    curve_funcs_derivs = [lambda t: np.exp(t), lambda t: -np.sin(t), lambda t: 7 * t ** 6]
    return curve_centre_of_mass(curve_funcs, curve_funcs_derivs, lambda *x: 1, 0, 1)


def task2():
    curve_func = [lambda t: t, lambda t: np.log10(t)]
    curve_func_derivs = [lambda t: 1, lambda t: 1/(t*np.log(10))]
    density_func = lambda x1, x2: x1 + np.exp(x2)
    length = curve_len(curve_func, curve_func_derivs, 1, 10)
    centre = curve_centre_of_mass(curve_func, curve_func_derivs, density_func, 1, 10)
    return length, centre


def _integrate_1(err, n):
    func = lambda t: t*np.exp(-4*t)*(1 + np.exp(2*t))**0.5
    A = 1 / err
    xarr = np.linspace(1, A, n)
    return integral(func, xarr)

def _integrate_2(err, n):
    func = lambda t: np.exp(-3*t) * (1 + np.exp(2*t))**0.5
    A = 1 / err
    xarr = np.linspace(1, A, n)
    return integral(func, xarr)


def task3():
    curve_funcs = [lambda t: t, lambda t: np.exp(t)]
    curve_funcs_derivs = [lambda t: 1, lambda t: np.exp(t)]
    density = lambda x1, x2: np.exp(-4*x1)
    mass = curve_mass(curve_funcs, curve_funcs_derivs, density, 1, 100)
    x1 = _integrate_1(0.01, 10**3)/mass
    x2 = _integrate_2(0.01, 10**3)/mass
    return x1, x2



if __name__ == '__main__':
    print('task 1.1:',task1_1())
    print('task 1.2:',task1_2())
    print('task 2:',task2())
    print('task 3:',task3())
    # task 1.1: 2.2654165458829105
    #
    # task 1.2: [2.000302780021017, 0.7596503741000319, 0.26815954687633614]
    #
    # task 2: (9.08347337985697, [6.54241806126943, 0.775911853205849])
    #
    # task 3: (1.4858534940910781, 4.4799336948084685)
    #