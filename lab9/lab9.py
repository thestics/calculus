import numpy as np

sin = np.sin
cos = np.cos
pi = np.pi

def task1(n):
    f = lambda x1, x2: x1**4 + x2**4 <= 1
    rho = lambda x1, x2: 2 - x1**2 - x2**2
    amt = 1 << (n + 1)
    inner_pts = []
    for x0 in np.linspace(-1, 1, amt - 1):
        for y0 in np.linspace(-1, 1, amt - 1):
            delta = 1 / (1 << n)
            mid = (x0 + delta / 2, y0 + delta / 2)
            if f(*mid):
                inner_pts.append(mid)
    total = 0
    for p in inner_pts:
        total += rho(*p) * (1 / (1 << n)) ** 2
    return total

# 5.154894483540318

def task2(n):
    f = lambda x1, x2, x3: x1**2 + x2**2 <= 1 and abs(x3) <= 2
    rho = lambda x1, x2, x3: x1**2 + x2**2 + x3**2
    amt = 1 << (n + 1)
    inner_pts = []
    for x0 in np.linspace(-1, 1 - 1/amt, amt):
        for y0 in np.linspace(-1, 1 - 1/amt, amt):
            for z0 in np.linspace(-2, 2 - 1/amt,  2 * amt):
                delta = 1 / (1 << n)
                mid = (x0 + delta/2, y0 + delta/2, z0 + delta/2)
                if f(*mid):
                    inner_pts.append(mid)
    total = 0
    for p in inner_pts:
        total += rho(*p) * (1 / (1 << n)) ** 3
    return total
# 22.90668352450202

def task3(n):
    center = (_int1(n), _int2(n), _int3(n))
    return center
# (0.09835035679861903, 0.09835035679861903, 0.06556392787024379)

def _int1(n):
    f = lambda x1, x2, x3: x1 ** 2 + x2 ** 2 + x3 ** 2 <= 1 and \
                           x1 >= 0 and x2 >= 0 and x3 >= 0
    rho = lambda x1, x2, x3: x1* (x1 ** 2 + x2 ** 2)
    amt = 1 << n
    inner_pts = []
    for x0 in np.linspace(0, 1 - 1 / amt, amt):
        for y0 in np.linspace(0, 1 - 1 / amt, amt):
            for z0 in np.linspace(0, 1 - 1 / amt, amt):
                delta = 1 / (1 << n)
                mid = (x0 + delta / 2, y0 + delta / 2, z0 + delta / 2)
                if f(*mid):
                    inner_pts.append(mid)
    total = 0
    for p in inner_pts:
        total += rho(*p) * (1 / (1 << n)) ** 3
    return total


def _int2(n):
    f = lambda x1, x2, x3: x1 ** 2 + x2 ** 2 + x3 ** 2 <= 1 and \
                           x1 >= 0 and x2 >= 0 and x3 >= 0
    rho = lambda x1, x2, x3: x2* (x1 ** 2 + x2 ** 2)
    amt = 1 << n
    inner_pts = []
    for x0 in np.linspace(0, 1 - 1 / amt, amt):
        for y0 in np.linspace(0, 1 - 1 / amt, amt):
            for z0 in np.linspace(0, 1 - 1 / amt, amt):
                delta = 1 / (1 << n)
                mid = (x0 + delta / 2, y0 + delta / 2, z0 + delta / 2)
                if f(*mid):
                    inner_pts.append(mid)
    total = 0
    for p in inner_pts:
        total += rho(*p) * (1 / (1 << n)) ** 3
    return total


def _int3(n):
    f = lambda x1, x2, x3: x1 ** 2 + x2 ** 2 + x3 ** 2 <= 1 and \
                           x1 >= 0 and x2 >= 0 and x3 >= 0
    rho = lambda x1, x2, x3: x3 * (x1 ** 2 + x2 ** 2)
    amt = 1 << n
    inner_pts = []
    for x0 in np.linspace(0, 1 - 1 / amt, amt):
        for y0 in np.linspace(0, 1 - 1 / amt, amt):
            for z0 in np.linspace(0, 1 - 1 / amt, amt):
                delta = 1 / (1 << n)
                mid = (x0 + delta / 2, y0 + delta / 2, z0 + delta / 2)
                if f(*mid):
                    inner_pts.append(mid)
    total = 0
    for p in inner_pts:
        total += rho(*p) * (1 / (1 << n)) ** 3
    return total


def mass(n):
    pts = []
    area = lambda r, phi, psi: r ** 2 * (cos(phi)**4 + sin(phi)**4 + cos(psi)**4 + sin(psi)**4)
    density = lambda r, phi, psi: phi**2 + psi**2
    amt = (1 << n) - 1
    delta = 1 / (1 << n + 1)
    side = 1/(1 << n)
    for phi in np.linspace(0, 2*pi, 2 * amt):
        for psi in np.linspace(-pi/2, pi/2, amt):
            for r in np.linspace(0, 0.5, amt):
                mid = (r + delta, phi + delta, psi + delta)
                if area(*mid):
                    pts.append((r, phi, psi))
    res = sum([density(*p)*side**3 for p in pts])
    return res
# 25.719166761396842


def _int1_1(n, mass):
    pts = []
    area = lambda r, phi, psi: r ** 2 * (cos(phi) ** 4 + sin(phi) ** 4 + cos(psi) ** 4 + sin(psi) ** 4)
    density = lambda r, phi, psi: (r**2*cos(psi)) * (r*cos(psi)*cos(phi)) * (phi ** 2 + psi ** 2)   # Jacobean + x1 in spherical + density func
    amt = (1 << n) - 1
    delta = 1 / (1 << n + 1)
    side = 1 / (1 << n)
    for phi in np.linspace(0, 2 * pi, 2 * amt):
        for psi in np.linspace(-pi / 2, pi / 2, amt):
            for r in np.linspace(0, 0.5, amt):
                mid = (r + delta, phi + delta, psi + delta)
                if area(*mid):
                    pts.append((r, phi, psi))
    res = sum([density(*p) * side ** 3 for p in pts])
    return res/mass


def _int2_1(n, mass):
    pts = []
    area = lambda r, phi, psi: r ** 2 * (cos(phi) ** 4 + sin(phi) ** 4 + cos(psi) ** 4 + sin(psi) ** 4)
    density = lambda r, phi, psi: (r**2*cos(psi)) * (r*cos(psi)*sin(phi)) * (phi ** 2 + psi ** 2)        # Jacobean + x2 in spherical + density func
    amt = (1 << n) - 1
    delta = 1 / (1 << n + 1)
    side = 1 / (1 << n)
    for phi in np.linspace(0, 2 * pi, 2 * amt):
        for psi in np.linspace(-pi / 2, pi / 2, amt):
            for r in np.linspace(0, 0.5, amt):
                mid = (r + delta, phi + delta, psi + delta)
                if area(*mid):
                    pts.append((r, phi, psi))
    res = sum([density(*p) * side ** 3 for p in pts])
    return res/mass


def _int3_1(n, mass):
    pts = []
    area = lambda r, phi, psi: r ** 2 * (cos(phi) ** 4 + sin(phi) ** 4 + cos(psi) ** 4 + sin(psi) ** 4)
    density = lambda r, phi, psi: (r**2*cos(psi))*(r*sin(psi))*(phi ** 2 + psi ** 2)
    amt = (1 << n) - 1
    delta = 1 / (1 << n + 1)
    side = 1 / (1 << n)
    for phi in np.linspace(0, 2 * pi, 2 * amt):
        for psi in np.linspace(-pi / 2, pi / 2, amt):
            for r in np.linspace(0, 0.5, amt):
                mid = (r + delta, phi + delta, psi + delta)
                if area(*mid):
                    pts.append((r, phi, psi))
    res = sum([density(*p) * side ** 3 for p in pts])
    return res/mass


def task4(n):
    m = mass(n)
    x1 = _int1_1(n, m)
    x2 = _int2_1(n, m)
    x3 = _int3_1(n, m)
    return x1, x2, x3
# (0.002533047339425227, -0.006822791107117372, 4.591197140739783e-19)




if __name__ == '__main__':
    print(task4(5))