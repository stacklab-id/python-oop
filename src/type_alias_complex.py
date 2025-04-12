from typing import List, Tuple

Matrix = List[Tuple[int, int]]

def sum_matrix(m1: Matrix, m2: Matrix) -> Matrix:
    return [
        (x1 + x2, y1 + y2)
        for (x1, x2), (y1, y2) in zip(m1, m2)
    ]

matrix_1: Matrix = [(1, 2), (3, 4), (1, 1)]
matrix_2: Matrix = [(2, 2), (3, 2), (4, 2)]

result = sum_matrix(matrix_1, matrix_2)
print(result)

