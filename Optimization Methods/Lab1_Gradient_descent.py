import numpy as np
import random
import numpy.linalg as linalg

step = 1e-2
eps = 1e-4
max_iters = 30000

f = lambda x: 0.5 * (x.T @ A @ x) + (b @ x)
f_ = lambda x: A @ x + b

def analytical_solution():
    return linalg.solve(A, -b)

def Gradient(x):    #Метод градиентного спуска
    iters = 0
    while (np.linalg.norm(f_(x)) > eps):
        #print("{}) F = {:.6f} x = {}".format(iters, f(x), x))
        x = x - step * f_(x)
        iters += 1
        if (iters > max_iters): 
            break
    
    an = analytical_solution()
    print()
    print("x_min = \n", x)
    print("analytical solution = \n", an)
    print("F(x_min) = \n", f(x))
    print("Error_x = \n", linalg.norm(an - x))
    print("Error_y = \n", linalg.norm(f(an) - f(x)))
    return x

def Newton(x):  #Метод Ньютона
    iters = 0
    H = linalg.inv(A)

    while (np.linalg.norm(f_(x)) > eps):
        print("{}) F = {:.6f} x = {}".format(iters, f(x), x))
        x = x - H @ f_(x)
        iters += 1
        if (iters > max_iters): 
            break

    an = analytical_solution()
    print()
    print("x_min = \n", x)
    print("analytical solution = \n", an)
    print("F(x_min) = \n", f(x))
    print("Error_x = \n", linalg.norm(an - x))
    print("Error_y = \n", linalg.norm(f(an) - f(x)))
    return x

def Kunn_Takker(x):
    A_vec = np.column_stack((A, c))
    A_vec = np.row_stack((A, c))

n = 6
d = 0
c = np.array([2, 3, 4, 3, 4, 1])
b = np.array([1, 8, 1, 8, 1, 5])
A = np.array([[13, 3, 6, 5, 12, 8],[3, 4, 6, 1, 8, 2],[6, 6, 11, 2, 13, 3],[5, 1, 2, 5, 6, 2],[12, 8, 13, 6, 21, 7],[8, 2, 3, 2, 7, 6]])
x = np.ones((6))

#while True:
#    B = np.array([[random.randint(0, 2) for i in range(n)] for j in range(n)])
#    if linalg.det(B) != 0:
#        A = B.transpose() @ B
#        print("Eigenvalues = \n", linalg.eigvals(A))
#        assert(np.all(linalg.eigvals(A) > 0))
#        break

print ("Matrix A: \n", A)
print ("Vector B:\n", b)
x = Gradient(x)
print(x)

while True:
    d = random.randint(1, 100)
    if (c @ x + d > 0):
        print ("d =", d)
        break;



A_vec = np.column_stack((A, c))
A_vec = np.row_stack((A_vec, np.append(c,0)))
print ("\n", A_vec)
#Newton(x)