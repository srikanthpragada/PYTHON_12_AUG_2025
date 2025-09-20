from threading import Thread
import threading


def print_numbers():
    for i in range(1, 11):
        print(i)


t1 = Thread(target = print_numbers)
t1.start()
print('End of Main')
