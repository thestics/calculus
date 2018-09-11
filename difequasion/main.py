import numpy as np
import matplotlib.pyplot as plt


def square_exp(t0, t1, n):
    x0 = 0
    res = [x0]
    for i in range(n, 0, -1):
        x1 = x0 + i**2
        res.append(x1)
        x0 = x1
    length = abs(res[-1] - res[0])
    res = np.array(res)
    res = res/length * (t1 - t0)
    return res



def diffeq(g, t0, t1, y0, k):
    # delta = 0.1
    # span = np.linspace(t0, t1, int((t1-t0)/delta))
    span = np.array(square_exp(t0, t1, 100))
    # print(span)
    res = []
    prevx = span[0]
    res.append(y0)
    for x in span[1:]:
        delta = abs(x - prevx)
        print(delta, end='\n')
        y1 = delta*(k*y0 + g(x)) + y0
        res.append(y1)
        y0 = y1
        prevx = x
    return span, np.array(res)


if __name__ == '__main__':
    g = lambda x: 3*x**2 - 2*x**3
    t0 = 0
    t1 = 5
    y0 = 0
    k = 2
    span, res = diffeq(g, t0, t1, y0, k)
    # print(span, res)
    plt.plot(span, res)
    plt.plot(span, span**3)
    plt.show()
    # print(list(square_exp(0, 5, 10)))
