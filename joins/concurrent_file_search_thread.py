import os
from os.path import isdir, join
from threading import Lock, Thread

MATCHES = []
MUTEX = Lock()

def search(directory: str, target: str, found: list[str]):
    print(f"Searching in: {directory}")
    child_threads = []

    for file in os.listdir(directory):
        if target in file:
            MUTEX.acquire()
            found.append(join(directory, file))
            MUTEX.release()
        elif isdir(join(directory, file)):
            sub_worker = Thread(target=search, args=(join(directory, file), target, found))
            sub_worker.start()
            child_threads.append(sub_worker)

    for sub_worker in child_threads:
        sub_worker.join()

if __name__ == "__main__":
    dir_to_search = "/home/sebastian/Documents"
    file_to_search = "README.md"
    worker = Thread(target=search, args=(dir_to_search, file_to_search, MATCHES))
    worker.start()
    worker.join()  # Wait for thread to be done

    for match in MATCHES:
        print(f"Match: {match}")