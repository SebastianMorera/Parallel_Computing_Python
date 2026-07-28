import time
from queue import Queue
from threading import Thread


def consumer(q):
    while True:
        item = q.get()
        print(f"Consumed {item}")
        time.sleep(1)


def producer(q):
    while True:
        q.put("Hello there")
        print("Message sent")


if __name__ == "__main__":
    q = Queue(maxsize=10)
    t1 = Thread(target=consumer, args=(q,))
    t2 = Thread(target=producer, args=(q,))
    t1.start()
    t2.start()
