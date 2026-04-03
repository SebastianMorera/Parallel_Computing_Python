import os
from os.path import isdir, join

MATCHES = []

def search(directory: str, target: str, found: list[str]):
    print(f"Searching in: {directory}")
    for root, dirs, files in os.walk(directory):
        if target in files:
            found.append(join(root, target))

if __name__ == "__main__":
    dir_to_search = "/home/sebastian/Documents"
    file_to_search = "README.md"
    search(dir_to_search, file_to_search, MATCHES)

    for match in MATCHES:
        print(f"Match: {match}")