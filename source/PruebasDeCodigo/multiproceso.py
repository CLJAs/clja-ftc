import multiprocessing
import os
from multiprocessing import Process


def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())


def f(name, numero):
    info('function f')
    print('hello', name, numero)


if __name__ == '__main__':
    info('main line')
    p = Process(target=f, args=('bob', 33,))
    p.start()
    p.join()
    numero_de_hilos = multiprocessing.cpu_count()
    print ("Esta CPU tiene: ", str(numero_de_hilos), " hilos!!")
