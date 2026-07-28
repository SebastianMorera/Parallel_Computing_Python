import time
from multiprocessing import Process, Queue


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
    p1 = Process(target=consumer, args=(q,))
    p2 = Process(target=producer, args=(q,))
    p1.start()
    p2.start()
