import json
import urllib.request
import time
from typing import Dict
from threading import Thread, Lock

FINISHED_WORKERS = 0

def count_letters(url: str, frequency: Dict[str, int], mutex: Lock):
    with urllib.request.urlopen(url) as response:
        content = response.read().decode('utf-8')
        mutex.acquire()
        for letter in content:
            if letter.isalpha():
                frequency[letter.lower()] += 1

        global FINISHED_WORKERS
        FINISHED_WORKERS += 1
        mutex.release()

def main():
    frequency = {}
    mutex = Lock()

    for c in "abcdefghijklmnopqrstuvwxyz":
        frequency[c] = 0

    start = time.time()
    for i in range(1000, 1020):
        Thread(target=count_letters, args=(f"https://www.rfc-editor.org/rfc/rfc{i}.txt", frequency, mutex)).start()

    while True:
        with mutex:
            if FINISHED_WORKERS == 20:
                break
        time.sleep(0.1)

    end = time.time()
    print(json.dumps(frequency, indent=4))
    print(f"Time taken: {end - start}")

if __name__ == "__main__":
    main()
