from __future__ import print_function

from ipywidgets import interact, interactive, fixed, interact_manual
import numpy as np
#from tqdm import tqdm

def f(x):
    return 1 / np.exp(-x[0]*x[1])

def fw(x):
    return ((x[1] * np.exp(-x[0]*x[1])) / (1 + np.power(np.exp(-x[0]*x[1]), 2)))
            
def fx(x):
    return ((x[0] * np.exp(-x[0]*x[1])) / (1 + np.power(np.exp(-x[0]*x[1]), 2)))

def gradient_descent(alpha=0.01, eps=0.001):
    x_prev = np.array([100, 100])  # начальная инициализация
    x = np.array([1, 1])  # начальная инициализация
    for _ in range(100000):
        print(_)  # смотрим, на каком мы шаге
        if np.sum((x - x_prev)**2) < eps**2:  # условие остановки
            break
        x_prev = x
        x = x_prev - alpha * np.array(fw(x_prev), fx(x_prev))  # по формуле выше
    return x
x_min = gradient_descent()
f(x_min)