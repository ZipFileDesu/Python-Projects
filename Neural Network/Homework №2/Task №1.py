import numpy as np
#import pandas as pd
#import matplotlib as pyplot

#from scipy import ndimage  # спецификатор для работы с изображениями
#from scipy import misc
#from PIL import Image

#%matplotlib inline

# Для генерации матриц используем фукнцию random -- она используется для генерации случайных объектов
# функция sample создает случайную выборку. В качестве аргумента ей передается кортеж (i,j), здесь i -- число строк,
# j -- число столбцов.
a = np.random.sample((10,10))
b = np.random.sample((10,10))

#a = np.array(([2, -3], [4, -6]))
#b = np.array(([9, -6], [6, -4]))

# выведите размерность (ранг) каждой матрицы с помощью функции ndim.
# Используйте функцию shape, что она вывела?
# ========
# тут можно писать код
# ========
print("A: \n", a)
print("B: \n", b)

print ("ndim A:", a.ndim)
print ("ndim B:", b.ndim)
print ("shape A:", a.shape)
print ("shape B:", b.shape)

print (a @ b)

for k in range (len (a)):
    for i in range (len(a)):
        result = 0
        for j in range(len(a)):
            result += a[k][j] * b[j][i]
        print (round (result, 5), end = " ")
    print()

