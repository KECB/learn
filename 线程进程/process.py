import os
import time
import random
from multiprocessing import Process
from multiprocessing import Pool


# 子进程要执行的代码
def run_proc(name, count):
    print('Run child process %s %s (%s)...' % (name, count, os.getpid()))


def long_time_task(name):
    print('Run task %s (%s) ...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, end - start))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    # p = Process(target=run_proc, args=('test', '1', ))
    # print('Child process will start.')
    # p.start()
    # p.join()
    # print('Child process end.')
    p = Pool(17)
    for i in range(18):
        p.apply_async(long_time_task, args=(i, ))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
