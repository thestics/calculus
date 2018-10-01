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


def build_tangent_surf(A, B, C, x0, y0, z0):
    """
    Builds a tangent plane to surface
    """
    res = lambda x, y: (A * (x - x0) + B * (y - y0) + C * z0) / C
    return res


def test3(x0):
    """
    For two-variables function builds a tangent plane at point x0 = (x0(1), x0(2))

    :return:
    """
    f = lambda x1, x2: x1**2 + x2**4
    x0 = (1, 1)
    A = part_diff(f, x0, 0)
    B = part_diff(f, x0, 1)
    z0 = f(*x0)
    tangent_surf_func = build_tangent_surf(A, B, -1, *x0, z0)   # C == -1 because df/dz for this func equals -1
    return tangent_surf_func