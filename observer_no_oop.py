def attach(observers, observer):
    observers.append(observer)


def detach(observers, observer):
    observers.remove(observer)


def notify(observers):
    for observer in observers:
        observer()


def observer1_update():
    print("ConcreteObserver1: Обновление получено ")


def observer2_update():
    print("ConcreteObserver2: Обновление получено")


def run_no_oop():
    observers = []

    attach(observers, observer1_update)
    attach(observers, observer2_update)

    notify(observers)

    detach(observers, observer2_update)

    notify(observers)


if __name__ == '__run_no_oop__':
    run_no_oop()

