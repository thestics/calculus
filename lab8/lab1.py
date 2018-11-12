import numpy as np
from random import random



def recursive_iter(n, iterable):
    """
    Plays role of n-times 'for' on 'iterable' items

    :return All n-combinations form iterable elements
    """

    res = []

    def _rec(n, collec, iterable):
        if len(collec) == n:
            res.append(tuple(collec[:]))
            collec.pop()
            return
        for i in range(len(iterable)):
            collec.append(iterable[i])
            _rec(n, collec, iterable)
        if collec:
            collec.pop()

    _rec(n, [], iterable)
    return res


def test1_naive(n):
    f = lambda x, y: x**4 + y**4 <= 1
    a = (-1, 1)
    b = (-1, 1)
    amt1 = abs(a[1] - a[0]) * (1 << n)  # (b-a)*2^n
    amt2 = abs(b[1] - b[0]) * (1 << n)
    inner = 0                           # внутреннее
    outer = 0                           # внешнее
    for x0 in np.linspace(a[0], a[1], amt1 -1):
        for y0 in np.linspace(b[0], b[1], amt2 - 1):
            # print(x0, y0)
            delta = 1/(1 << n)
            lDown = (x0, y0)
            lUp = (x0, y0 + delta)
            rDown = (x0 + delta, y0)
            rUp = (x0 + delta, y0 + delta)
            mid = (x0 + delta/2, y0 + delta/2)
            points = [lDown, lUp, rDown, rUp, mid]
            if any([f(*p) for p in points]):    # if any of points satisfies equation (in area or intersects area)
                outer += 1/(1 << (2 * n))
            if all([f(*p) for p in points]):    # if all points satisfies equation (strictly IN area)
                inner += 1/(1 << (2 * n))
    return inner, outer, outer - inner

#  res, error
# (3.015625, 0.3828125)
# (3.5205078125, 0.11181640625)
# (3.661956787109375, 0.02935791015625)


def test1_monte_carlo(n):
    f = lambda x, y: x ** 4 + y ** 4 <= 1
    a = (-1, 1)
    b = (-1, 1)
    pts = [(random() * 2 - 1, random() * 2 - 1) for i in range(n)]
    inner_pts = [p for p in pts if f(*p)]
    big_area = 4
    factor = len(inner_pts)/len(pts)
    small_area = big_area * factor
    return small_area

# 3.92
# 3.752
# 3.7048


def test2_naive(n):
    f = lambda x, y, z: x ** 2 + y ** 2 <= 1 and z == 0 or\
                        x ** 2 + y ** 2 <= 1 and x + y - z <= 0 or \
                        x ** 2 + y ** 2 <= 1 and 2 * y + 2 * z >= 0
    a = (-1, 1)
    b = (-1, 1)
    c = (-1.5, 1)   # between -2*0.5 and 1
    amt1 = (a[1] - a[0]) * (1 << n)
    amt2 = (b[1] - b[0]) * (1 << n)
    amt3 = (c[1] - c[0]) * (1 << n)
    inner = 0
    outer = 0
    for x0 in np.linspace(a[0], a[1], amt1 - 1):
        for y0 in np.linspace(b[0], b[1], amt2 - 1):
            for z0 in np.linspace(c[0], c[1], amt3 - 1):
                delta = 1/(1 << n)
                mid = (x0 + delta / 2, y0 + delta / 2, z0 + delta / 2)
                points = [      # points of unit block for certain space fragmentation
                    (x0, y0, z0), (x0, y0 + delta, z0), (x0 - delta, y0 + delta, z0), (x0 - delta, y0, z0),
                    (x0, y0, z0 + delta), (x0, y0 + delta, z0 + delta), (x0 - delta, y0 + delta, z0 + delta), (x0 - delta, y0, z0 + delta),
                    mid
                ]
                if any([f(*p) for p in points]): # if any of points satisfies equation (in area or intersects area)
                    outer += 1/(1 << 3*n)
                if all([f(*p) for p in points]): # if all points satisfies equation (strictly in area)
                    inner += 1/(1 << 3*n)
    return inner, outer, outer - inner

# res, err
# (3.765625, 2.3125) n = 2
# (4.71142578125, 1.2099609375) n = 4


def test2_monte_carlo(n):
    f = lambda x, y, z: x ** 2 + y ** 2 <= 1 and z == 0 or \
                        x ** 2 + y ** 2 <= 1 and x + y - z <= 0 or \
                        x ** 2 + y ** 2 <= 1 and 2 * y + 2 * z >= 0
    pts = [(random() * 2 - 1, random() * 2 - 1, random() * 2.5 - 1.5) for i in range(n)]
    inner_pts = [p for p in pts if f(*p)]
    big_area = 10
    factor = len(inner_pts)/len(pts)
    small_area = big_area * factor
    return small_area
# 4.5
# 4.61
# 4.6401

def integrate_naive(n):
    f1 = lambda x, y: np.sin(np.exp(x - y))
    f2 = lambda x, y: x**4 + y**4 <= 1
    amt = 1 << (n + 1)
    inner_pts = []
    for x0 in np.linspace(-1, 1, amt - 1):
        for y0 in np.linspace(-1, 1, amt - 1):
            delta = 1 / (1 << n)
            mid = (x0 + delta / 2, y0 + delta / 2)
            if f2(*mid):
                inner_pts.append(mid)
    total = 0
    for p in inner_pts:
        total += f1(*p) * (1 << n) ** 2
    return total


def integrate_monte_carlo(n):
    f1 = lambda x, y: np.sin(np.exp(x - y))
    f2 = lambda x, y: x ** 4 + y ** 4 <= 1
    pts = [(random() * 2 - 1, random() * 2 - 1) for i in range(n)]
    inner_pts = [p for p in pts if f2(*p)]
    mA = test1_monte_carlo(n)
    factor = sum([f1(*p) for p in inner_pts]) / len(inner_pts)
    return factor * mA


def task3_1(m, n):
    f = lambda *xarr: sum([x**2 for x in xarr]) <= 0.25
    pts = [tuple([random() - 0.5 for i in range(m)]) for i in range(n)]
    inner_pts = [p for p in pts if f(*p)]
    outer_size = 1
    factor = len(inner_pts) / len(pts)
    inner_size = outer_size * factor
    return inner_size


def task3_2(m, n):
    f = lambda *xarr: sum([x ** 2 for x in xarr]) <= 0.25
    measure = 0
    amt = 1 << n
    side = 1 / (1 << n)                     # length of brick side
    seq = np.linspace(-0.5, 0.5, amt + 1)      # len of segment is 2, and needed to be divided into segments len 1/2^n
    delta = 1 / (1 << n + 1)                        # half of brick side length
    for p in recursive_iter(m, seq):
        center = tuple(map(lambda x: x + delta, p))
        if f(*center):
            measure += side**m
    return measure


if __name__ == '__main__':
    print(integrate_naive(2))
    print(integrate_monte_carlo(100))