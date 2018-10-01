import numpy as np
from math import log


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


def main(n):
    f = lambda x1, x2: (x1 - x2 + 1) * np.sin(x1 + x2)
    res = 0
    x0 = (0, 0)
    x = (0.1, 0.05)
    for i in range(n):  # all terms in Taylor's formula
        derivs = build_all_partions(i, 2)
        for d in derivs:
            val = nth_part_diff(f, list(x0), tuple(d))
            a = 1
            for i in range(len(x)):
                a *= x[i] - x0[i]
            val *= a
            res += val
    return res







if __name__ == '__main__':
    print(main(2))