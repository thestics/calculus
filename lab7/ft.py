# при умножении многочленов, делать запас степеней с помощью нулевых коэфициентов до степени 2n


import numpy as np


I = complex('j')


def gn(n, fn: list):
    sm = 0
    for k, fk in enumerate(fn):
        sm += fk * np.exp((-2*I*np.pi*k*n)/len(fn))
    return sm


def fn(n, gn: list):
    sm = 0
    for k, gk in enumerate(gn):
        sm += gk * np.exp((2*I*np.pi*k*n)/len(gn))
    return sm/len(gn)


def discrete_fourier_transform(f_lst: list):
    return [gn(n, f_lst) for n in range(len(f_lst))]


def inv_discrete_fourier_transform(g_lst: list):
    return [fn(n, g_lst) for n in range(len(g_lst))]


if __name__ == '__main__':
    s = [1, 2, 3]
    dft = discrete_fourier_transform(s)
    idft = inv_discrete_fourier_transform(dft)
    print(dft)
    print(idft)


