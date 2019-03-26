import multiprocess


class multi():
    def __init__(self, iterable):
        self.process = 4


def time_measure(func, arg):
    start = time.time()
    result = func(arg)
    end = time.time()
    print("Time taken is {}".format(end-start))
    return result





from multiprocess import Pool
import time

start_time = time.time()

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


def print_fibo(n, fibo=fibo):  # 피보나치 결과를 확인합니다.
    print(fibo(n))


num_list = [31, 32, 33, 34]

pool = Pool(processes=4)  # 4개의 프로세스를 사용합니다.
pool.map(print_fibo, num_list)  # pool에 일을 던져줍니다.

print("--- %s seconds ---" % (time.time() - start_time))




from multiprocess import Process, Queue

def f(q):
    q.put('hello world')

if __name__ == '__main__':
    q = Queue()
    p = Process(target=f, args=[q])
    p.start()
    print (q.get())
    p.join()





import time

start_time = time.time()

def fibo(n): # 회귀적 피보나치 함수
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

num_list = [31, 32, 33, 34]
result_list = []
for num in num_list:
    result_list.append(fibo(num))

print(result_list)
print("--- %s seconds ---" % (time.time() - start_time))


from multiprocessing import Process
import os

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f(name):
    info('function f')
    print('hello', name)

if __name__ == '__main__':
    freeze_support()
    info('main line')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()