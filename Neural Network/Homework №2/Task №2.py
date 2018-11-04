import numpy as np
from scipy.stats import uniform

# функция, решающая задачу с помощью NumPy
def sec_av(A):
    S = np.nancumsum(A) / np.array(range(1, len(A) + 1))
    return S

# функция без NumPy
def stupid_sec_av(A):
    S = [0 for i in range(len(A))]
    for i in range(len(A)):
        for j in range(i + 1):
            S[i] += A[j] / (i + 1)
    return S

# зададим некоторую последовательность и проверим ее на ваших функциях.
# Первая функция должна работать ~ в 50 раз быстрее
A = uniform.rvs(size = 10)

S1 = sec_av(A)
S2 = stupid_sec_av(A)
print (S1)
print (S2)
#проверим корректность:
print (np.abs(S1 - S2).sum())