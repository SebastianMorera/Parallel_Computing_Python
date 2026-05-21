import os
from os.path import isdir, join
from threading import Lock, Thread
from wait_group import WaitGroup

MATCHES = []
MUTEX = Lock()


def search(directory: str, target: str, wg: WaitGroup):
    print(f"Searching in: {directory}")

    for file in os.listdir(directory):
        full_path = join(directory, file)
        if target in file:
            MUTEX.acquire()
            MATCHES.append(full_path)
            MUTEX.release()
        elif isdir(full_path):
            wg.add(1)
            sub_worker = Thread(target=search, args=(full_path, target, wg))
            sub_worker.start()
    wg.done()


if __name__ == "__main__":
    dir_to_search = "/home/sebastian/Documents"
    file_to_search = "README.md"

    wait_group = WaitGroup()
    wait_group.add(1)
    worker = Thread(target=search, args=(dir_to_search, file_to_search, wait_group))
    worker.start()
    wait_group.wait()

    for match in MATCHES:
        print(f"Match: {match}")
