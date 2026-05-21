import time
from threading import Thread, Condition


class StingySpendy:
    money = 100
    cv = Condition()

    def stingy(self):
        for i in range(1000000):
            self.cv.acquire()
            self.money += 10
            self.cv.notify()
            self.cv.release()
        print("Stingy thread finished\n")

    def spendy(self):
        for i in range(500000):
            self.cv.acquire()
            while self.money < 20:
                self.cv.wait()
            self.money -= 20
            self.cv.release()
        print("Spendy thread finished\n")


if __name__ == "__main__":
    ss = StingySpendy()
    Thread(target=ss.stingy, args=()).start()
    Thread(target=ss.spendy, args=()).start()
    time.sleep(5)
    print(f"Money at the end: {ss.money}")
