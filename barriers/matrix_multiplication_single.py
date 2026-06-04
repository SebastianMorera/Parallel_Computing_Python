import time
from random import Random
from typing import List

matrix_size = 200
matrix_a = [[0] * matrix_size for a in range(matrix_size)]
matrix_b = [[0] * matrix_size for b in range(matrix_size)]
random = Random()


def generate_random_matrix(matrix: List) -> None:
    for r in range(matrix_size):
        for c in range(matrix_size):
            matrix[r][c] = random.randint(-5, 5)


if __name__ == "__main__":
    start = time.time()
    for t in range(10):
        generate_random_matrix(matrix_a)
        generate_random_matrix(matrix_b)
        result = [[0] * matrix_size for r in range(matrix_size)]

        for row in range(matrix_size):
            for col in range(matrix_size):
                for i in range(matrix_size):
                    result[row][col] += matrix_a[row][i] * matrix_b[i][col]

    end = time.time()
    print(f"Matrix a: {matrix_a}\nMatrix b: {matrix_b}\nResult: {result}")
    print(f"Done, time taken = {end - start}")
