import time
from random import Random
from threading import Barrier, Thread
from typing import List

matrix_size = 200
matrix_a = [[0] * matrix_size for a in range(matrix_size)]
matrix_b = [[0] * matrix_size for b in range(matrix_size)]
random = Random()
work_start = Barrier(matrix_size + 1)
work_complete = Barrier(matrix_size + 1)


def generate_random_matrix(matrix: List) -> None:
    for r in range(matrix_size):
        for c in range(matrix_size):
            matrix[r][c] = random.randint(-5, 5)


def work_out_row(r: int):
    while True:
        work_start.wait()
        for col in range(matrix_size):
            for i in range(matrix_size):
                result[r][col] += matrix_a[r][i] * matrix_b[i][col]
        work_complete.wait()


if __name__ == "__main__":
    for row in range(matrix_size):
        Thread(target=work_out_row, args=[row]).start()

    start = time.time()
    for t in range(10):
        generate_random_matrix(matrix_a)
        generate_random_matrix(matrix_b)
        result = [[0] * matrix_size for r in range(matrix_size)]
        work_start.wait()
        work_complete.wait()

    end = time.time()
    print(f"Matrix a: {matrix_a}\nMatrix b: {matrix_b}\nResult: {result}")
    print(f"Done, time taken = {end - start}")
