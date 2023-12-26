class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update()


class Observer:
    def update(self):
        pass


class ConcreteObserver1(Observer):
    def update(self):
        print("ConcreteObserver1: Обновление выполнено")


class ConcreteObserver2(Observer):
    def update(self):
        print("ConcreteObserver2: Обновление выполнено")


def run_oop():
    subject = Subject()

    observer1 = ConcreteObserver1()
    observer2 = ConcreteObserver2()

    subject.attach(observer1)
    subject.attach(observer2)

    subject.notify()

    subject.notify()


if __name__ == '__run_oop__':
    run_oop()

