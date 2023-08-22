import unittest
import numpy as np
from algoritmos.gauss import encontrar_pivo, eliminacao, decomposicao_LU, substituicao_retroativa, eliminacao_gauss

class TestMatrixOperations(unittest.TestCase):

    def test_encontrar_pivo(self):
        matrix = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
        self.assertEqual(encontrar_pivo(matrix), (1, 0))

    def test_eliminar_pivo_zero(self):
        matrix = np.array([[0, 1, 2], [0, 4, 5], [0, 7, 8]])
        expected_result = np.array([[0, 1, 2], [0, 7, 8], [0, 4, 5]])
        self.assertTrue(np.array_equal(eliminacao(matrix), expected_result))

    def test_decomposicao_LU(self):
        matrix = np.array([[2, 1, -1], [-3, -1, 2], [-2, 1, 2]])
        expected_L = np.array([[1, 0, 0], [-1.5, 1, 0], [-1, 0.5, 1]])
        expected_U = np.array([[-3, -1, 2], [0, 0.5, 0.5], [0, 0, 1]])
        expected_P = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
        L, U, P = decomposicao_LU(matrix)
        self.assertTrue(np.array_equal(L, expected_L))
        self.assertTrue(np.array_equal(U, expected_U))
        self.assertTrue(np.array_equal(P, expected_P))

    def test_substituicao_retroativa(self):
        matrix = np.array([[1, 2, 3, 6], [0, 1, 2, 3], [0, 0, 1, 1]])
        expected_result = [1, 1, 1]
        self.assertEqual(substituicao_retroativa(matrix), expected_result)

    def test_eliminar_gauss(self):
        A = np.array([[2, 1, -1], [-3, -1, 2], [-2, 1, 2]])
        b = np.array([8, -11, -3])
        expected_result = [2, 3, -1]
        self.assertEqual(eliminacao_gauss(A, b), expected_result)

import unittest
import numpy as np
from algoritmos.seidel import gauss_seidel

class TestGaussSeidel(unittest.TestCase):

    def test_gauss_seidel_solution(self):
        A = np.array([[4, -1, 0, 3], [1, 15.5, 3, 8], [0, -1.3, -4, 1.1], [14, 5, -2, 30]])
        b = np.array([1, 1, 1, 1])
        x0 = np.array([0, 0, 0, 0])
        max_iterations = 100
        epsilon = 1e-6
        
        expected_solution = np.linalg.solve(A, b)
        computed_solution = gauss_seidel(max_iterations, epsilon, x0, A, b)
        
        np.testing.assert_allclose(computed_solution, expected_solution, rtol=1e-5)

    def test_gauss_seidel_convergence(self):
        A = np.array([[4, 2, 0], [2, 5, 2], [0, 2, 4]])
        b = np.array([4, 2, 2])
        x0 = np.array([0, 0, 0])
        max_iterations = 100
        epsilon = 1e-6
        
        computed_solution = gauss_seidel(max_iterations, epsilon, x0, A, b)
        residual = np.linalg.norm(np.dot(A, computed_solution) - b)
        
        self.assertTrue(residual < epsilon)

if __name__ == '__main__':
    unittest.main()
