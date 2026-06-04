import time
from threading import Thread

def child():
    print("Child thread started")
    time.sleep(2)
    print("Child thread finished")

def parent():
    print("Parent thread started")
    child_thread = Thread(target=child, args=())
    child_thread.start()
    print("Parent thread waiting for child thread to finish")
    child_thread.join()
    print("Parent thread finished")

if __name__ == "__main__":
    parent()