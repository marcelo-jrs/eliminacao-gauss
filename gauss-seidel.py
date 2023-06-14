import numpy as np

def gauss_seidel(A, b, x0, epsilon=1e-5, max_iterations=100):
    n = len(A)
    x = np.copy(x0)
    
    for k in range(max_iterations):
        x_prev = np.copy(x)
        
        for i in range(n):
            sum1 = np.dot(A[i, :i], x[:i])
            sum2 = np.dot(A[i, i + 1:], x_prev[i + 1:])
            x[i] = (b[i] - sum1 - sum2) / A[i, i]
        
        if np.linalg.norm(x - x_prev) < epsilon:
            break
    
    return x

# Exemplo
A = np.array([[4.0, -1.0, 0.0], [1.0, 3.0, -1.0], [2.0, 0.0, 5.0]])
b = np.array([3.0, 6.0, -2.0])
x0 = np.array([0.0, 0.0, 0.0])



#1,08955224 - 1,35820895 -0,8358209

solution = gauss_seidel(A, b, x0, epsilon=1e-8)
print("Solução:", solution)


#  2,17910448 - 0,8358209