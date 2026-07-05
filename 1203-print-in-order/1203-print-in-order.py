import threading

class Foo:
    def __init__(self):
        self.cv = threading.Condition()
        self.turn = 0

    def first(self, printFirst):
        with self.cv:
            printFirst()
            self.turn = 1
            self.cv.notify_all()

    def second(self, printSecond):
        with self.cv:
            while self.turn != 1:
                self.cv.wait()
            printSecond()
            self.turn = 2
            self.cv.notify_all()

    def third(self, printThird):
        with self.cv:
            while self.turn != 2:
                self.cv.wait()
            printThird()