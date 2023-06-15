import numpy as np

def gauss_seidel(max_iterations, epsilon, x0, A, b):
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
