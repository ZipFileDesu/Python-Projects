import numpy as np
from scipy.stats import uniform

a = uniform.rvs(size = 10)
b = uniform.rvs(size = 10)

def stupid_scalar_product(a,b):
    print (a @ b)
    pass

def numpy_scalar_product(a,b):
    result = 0
    for i in range (len (a)):
        result += a[i]*b[i]
    print(result)
    pass

product_1 = stupid_scalar_product(a,b)
product_2 = numpy_scalar_product(a,b)
# проверим корректность:
np.abs(product_1 - product_2).sum()