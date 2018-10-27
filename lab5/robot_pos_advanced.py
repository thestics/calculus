"""
Пусть есть робот, который может двигаться вперед-назад, влево-вправо и раворачиваться на месте
Также среди светильников на потолке есть четыре фиксированных, расположенных по углам комнаты, размеры которой также
заранее известны
"""

import numpy as np
from numpy import linalg
import random


pi = np.pi
arcsin = np.arcsin


def get_angle(x1, x2):
    if x1 > 0 and x2 > 0:
        return arcsin(x1)
    elif x1 > 0 and x2 < 0:
        return 2*pi - arcsin(x1)
    elif x1 < 0 and x2 > 0:
        return pi - arcsin(x1)
    elif x1 < 0 and x2 < 0:
        return pi + arcsin(x1)
    elif x1 == 0 and x2 == 1:
        return pi/2
    elif x1 == 0 and x2 == -1:
        return -pi/2
    elif x1 == 1 and x2 == 0:
        return 0
    elif x1 == -1 and x2 == 0:
        return pi


if __name__ == '__main__':
    for i in range(100):
        phi = random.random() * 2*pi
        x1 = np.sin(phi)
        x2 = np.cos(phi)
        phi2 = get_angle(x1, x2)
        print(x1, x2,phi,phi2)