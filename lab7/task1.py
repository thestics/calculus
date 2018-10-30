from lab7.ft import discrete_fourier_transform, inv_discrete_fourier_transform
from numpy.fft import fft, ifft
from numpy.polynomial import Polynomial as poly
import time


def _list_to_int(seq: list):
    """
    Considers seq as a list of integers in positional notation of number

    :return: number
    """
    total = 0
    fact = 1
    for i in range(len(seq)-1, -1, -1):
        total += int(seq[i]) * fact
        fact *= 10
    return total


def sub_task2(acoef: list, bcoef: list):   # direct product
    t1 = time.time()
    p1 = poly(acoef)
    p2 = poly(bcoef)
    prod = p1 * p2
    t = time.time() - t1
    print(f'sub_task2 Time elapsed: {t}')
    return list(prod.coef)


def sub_task1(acoef: list, bcoef: list):   # fast fourier transform
    t1 = time.time()
    total_len = len(acoef) + len(bcoef)
    aext = [0 for i in range(total_len - len(acoef) - 1)]
    bext = [0 for i in range(total_len - len(bcoef) - 1)]
    acoef.extend(aext)
    bcoef.extend(bext)
    dfta = fft(acoef)
    dftb = fft(bcoef)
    dftc = [dfta[i] * dftb[i] for i in range(len(dfta))]
    ccoef = ifft(dftc)
    ccoef = list(map(lambda x: round(x.real), ccoef))
    t = time.time() - t1
    print(f'sub_task1 Time elapsed: {t}')
    return ccoef


def task1(acoef: list, bcoef: list):    # discrete fourier transform
    t1 = time.time()
    total_len = len(acoef) + len(bcoef)
    aext = [0 for i in range(total_len - len(acoef) - 1)]
    bext = [0 for i in range(total_len - len(bcoef) - 1)]
    acoef.extend(aext)
    bcoef.extend(bext)
    dfta = discrete_fourier_transform(acoef)
    dftb = discrete_fourier_transform(bcoef)
    dftc = [dfta[i] * dftb[i] for i in range(len(dfta))]
    ccoef = inv_discrete_fourier_transform(dftc)
    ccoef = list(map(lambda x: round(x.real), ccoef))
    t = time.time() - t1
    print(f'sub_task 0 Time elapsed: {t}')
    return ccoef


def task2():
    numb1 = []
    numb2 = []
    for i in range(1, 101):
        numb1.extend(str(i))
    for i in range(100, -1, -1):
        numb2.extend(str(i))
    t = time.time()
    print(int(''.join(numb1)) * int(''.join(numb2)))
    print(time.time() - t)
    numb1 = list(map(lambda x: int(x), numb1))
    numb2 = list(map(lambda x: int(x), numb2))
    print(_list_to_int(task1(numb1, numb2)))
    print(_list_to_int(sub_task1(numb1, numb2)))


# task 1
# n == 200
# sub_task2 Time: 0.0
# sub_task1 Time: 0.00199
# sub_task0 Time: 6.43066


# n == 1000
# sub_task2 Time: 0.00199
# sub_task1 Time: 0.30908
# sub_task0 Time: >1m

# ---------------------------------------------

# task2
# python a*b: 0.0009980201721191406
# sub_task0: 1.6336588859558105
# sub_task1: 0.002990245819091797


if __name__ == '__main__':
    a = [i+1 for i in range(1000)]
    b = [200 - i for i in range(1000)]
    print(sub_task2(a, b))
    print(sub_task1(a, b))
    print(task1(a, b))
    task2()
