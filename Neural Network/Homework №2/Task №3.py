import numpy as np
import pandas as pd
import matplotlib as pyplot

from scipy import ndimage  # спецификатор для работы с изображениями
from scipy import misc
from scipy.stats import uniform
#from PIL import Image

# функция, решающая задачу с помощью NumPy
def transformation(X, a = 1):
    N = np.copy(np.flip(X, 0))
    np.place(N[1::2], N[1::2], 1)
    np.place(N[::2], N[::2], [x**3 for x in N[::2]])
    return X + N

# функция, решающая задачу  без NumPy
def stupid_transformation(X, a = 1):
    N = np.copy(X[::-1])
    N[1::2] = [a for _ in range(len(N[1::2]))]
    N[::2] = [x**3 for x in N[::2]]
    return X + N

X = uniform.rvs(size = 10) 

# здесь код эффективнее примерно в 20 раз. 
# если Вы вдруг соберетесь печатать массив без np -- лучше сначала посмотрите на его размер
print (X)
S1 = stupid_transformation(X)
print (S1)
S2 = transformation(X)
print (S2)
# проверим корректность:
#np.abs(S1 - S2).sum()