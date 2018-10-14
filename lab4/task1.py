import numpy as np


def build_all_partions(n, m):
    """
    Builds all possible fills of len M array with total sum n
    (all ways to find n-th derivative on func with m variables)
    """

    def _build_all_partions(n: int, m: int, current_arr: list, res):
        if sum(current_arr) == n and current_arr not in res:
            res.append(current_arr)
        elif sum(current_arr) == n and current_arr in res:
            return
        else:
            for i in range(len(current_arr)):
                new_arr = current_arr[:i] + [current_arr[i] + 1] + current_arr[i + 1:]
                _build_all_partions(n, m, new_arr, res)

    current = [0]*m
    res = []
    _build_all_partions(n, m, current, res)
    return res


def nth_part_diff(f: callable, x0: list, argnum_arr: tuple):
    """
    N-th partial derivative of func f at point x0, differentiated argnum[0] times on 1st arg,
    artnum[1] times on 2nd argument and so on
    """
    assert len(argnum_arr) > 0
    dx = 10**-5
    if sum(argnum_arr) == 0:
        return f(*x0)
    else:
        for i in range(len(argnum_arr)):
            if argnum_arr[i] != 0:
                number = i
                new_argnum_arr = *argnum_arr[:i],argnum_arr[i]-1,*argnum_arr[i+1:]
                break
        upd_x0 = x0[:i] + [x0[i] + dx] + x0[i+1:]
        up1 = nth_part_diff(f, upd_x0, new_argnum_arr)
        up2 = nth_part_diff(f, x0, new_argnum_arr)
        upper = up1 - up2
        return upper/dx


def part_diff(f, x0, argnum):
    """
    Partial derivative of func f at point x0 by argnumth's argument
    f(x, y), x0 = (1, 1), argnum = 1 will find df(x0)/dy
    """
    dx = 10**-5
    upper = f(*x0[:argnum], x0[argnum]+dx, *x0[argnum+1:]) - f(*x0)
    lower = dx
    return upper/lower


def minimize(err, mode, f, x0: list):
    """
    Minimize function

    :param err: error
    :param mode: 1 for min, -1 for max
    :return:
    """
    assert mode in (1, -1)
    # f = lambda x, y: mode*(2*x**2 + 3*y**2 - 4*x + 5*y - 1)
    # x0 = np.array([10, 10])
    gamma = 1
    n = 0
    while True:
        # print(x0)
        n += 1
        if n > 50:
            return list(x0)
        deriv = np.array([part_diff(f, x0, i) for i in range(len(x0))])
        x1 = np.array(x0) - gamma*deriv
        if f(*x1) >= f(*x0):
            gamma /= 2
            continue
        if gamma < err:
            return list(x1), n
        x0 = x1


def build_deriv_matrix(m):
    """
    Builds pseudo-Jacobian matrix for func, where on res[i][j] is amount of times which func is needed to be derived on
    each of the variables

    :param m: amount of variables in function
    :return:
    """
    partions = build_all_partions(2, m)
    res = []
    for i in range(m):
        row = [None] * i + partions[:m - i]
        partions = partions[m - i:]
        res.append(row)
    for i in range(len(res)):
        for j in range(len(res[i])):
            if res[i][j] is None:
                res[i][j] = res[j][i]
    return res


def _build_second_deriv(func, x0):
    derivs = build_deriv_matrix(len(x0))
    res = [[None for i in range(len(x0))] for j in range(len(x0))]
    for i, line in enumerate(derivs):
        for j, d in enumerate(line):
            res[i][j] = nth_part_diff(func, x0, d)
    return res


def task1newton(err, f: callable, x0: list):
    pass
    x0 = np.matrix([x0])
    n = 0
    while True:
        x0 = x0.tolist()[0]
        fact1 = np.matrix(_build_second_deriv(f, x0))**-1
        fact2 = np.matrix([part_diff(f, x0, i) for i in range(len(x0))])
        x1 = (np.array(x0) - fact2 * fact1).tolist()[0]
        if f(*tuple(x1)) >= f(*tuple(x0)):
            return x1, n
        if sum((np.array(x0) - np.array(x1))**2)**(1/2) < err:
            return x1, n
        n += 1
        x0 = np.matrix(x1)
        if n > 100:
            return


if __name__ == '__main__':
    f1 = lambda x, y: (2 * x ** 2 + 3 * y ** 2 - 4 * x + 5 * y - 1)
    x1 = ([10, 10])
    f2 = lambda x, y: x**2 + 2*y**2 - 4*y**4 - x**4+3
    x2 = ([10, 10], [10, -10], [-10, 10], [0.1, 0.1])
    f3 = lambda x, y: x**2 - y**2
    x3 = ([1, 1])
    f4 = lambda x, y, z: (x**2 + y**2 + z**2)**2 + ((x-2)**2 + (y - 2)**2 + (z - 2)**2)**2
    x4 = ([3,3,3], [-1,-2,-3], [1,1,1])
    #
    print(minimize(0.00000000001, 1, f1, x1))
    # print(build_all_partions(2, 4))
    # print(build_deriv_matrix(3))