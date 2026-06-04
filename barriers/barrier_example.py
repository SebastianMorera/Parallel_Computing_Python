import time
from threading import Barrier, Thread

barrier = Barrier(2)


def wait_on_barrier(name: str, time_to_sleep: int):
    for i in range(10):
        print(f"{name} running!")
        time.sleep(time_to_sleep)
        print(f"{name} is waiting on barrier")
        barrier.wait()
    print(f"{name} is finished.")


if __name__ == "__main__":
    red = Thread(target=wait_on_barrier, args=["red", 4])
    blue = Thread(target=wait_on_barrier, args=["blue", 10])
    red.start()
    blue.start()
    time.sleep(8)
    print(f"Aborting barrier!")
    barrier.abort()
