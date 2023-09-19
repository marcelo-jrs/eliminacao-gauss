import numpy as np
from algoritmos import seidel

max_iterations_TEST = 10
epsilon_TEST = 0.000001
b_TEST = np.array([4.0, 7.0, 3.0])
A_TEST = np.array([[4.0, 1.0, 2.0],
                    [3.0, 5.0, 1.0],
                    [1.0, 1.0, 3.0]])

x0_TEST = np.zeros_like(b_TEST)



resultado = seidel.gauss_seidel(max_iterations_TEST, epsilon_TEST, x0_TEST, A_TEST, b_TEST)
print(resultado)

""" 
    Para executar os testes rode o comando:

    coverage run -m pytest test_iterations.py

    Depois gere um relatório com o comando:

    coverage report -m

"""
