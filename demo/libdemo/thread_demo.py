from threading import Thread
import threading

class PrintThread(Thread):
    def run(self):
        for i in range(1,11):
            print(i)


print(threading.main_thread())
t1 = PrintThread()
t1.start()
print('End of Main')