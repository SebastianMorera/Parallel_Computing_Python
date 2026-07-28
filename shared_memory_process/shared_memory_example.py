import multiprocessing
from multiprocessing import Process

import time


def print_array_contents(array: list[int]):
    while True:
        print(*array, sep=", ")
        time.sleep(1)


if __name__ == "__main__":
    arr = multiprocessing.Array('i', [-1] * 10)
    process = Process(target=print_array_contents, args=([arr]))
    process.start()

    for j in range(10):
        time.sleep(2)
        for i in range(10):
            arr[i] = j
