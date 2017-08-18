import os
import time
import random
from multiprocessing import Process
from multiprocessing import Pool
from multiprocessing import Queue
import subprocess


# 子进程要执行的代码
def run_proc(name, count):
    print('Run child process %s %s (%s)...' % (name, count, os.getpid()))


def long_time_task(name):
    print('Run task %s (%s) ...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, end - start))


# 写数据进程
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C', 'D']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())


# 度数据进程
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)


if __name__ == '__main__':
    # print('Parent process %s.' % os.getpid())
    # p = Process(target=run_proc, args=('test', '1', ))
    # print('Child process will start.')
    # p.start()
    # p.join()
    # print('Child process end.')
    # p = Pool(17)
    # for i in range(18):
    #     p.apply_async(long_time_task, args=(i, ))
    # print('Waiting for all subprocesses done...')
    # p.close()
    # p.join()
    # print('All subprocesses done.')

    # print('$ nslookup www.python.org')
    # r = subprocess.call(['nslookup', 'www.python.org'])
    # print('Exit code:', r)
    # print('$ nslookup')
    # p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE,
    #                      stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
    # print(output.decode('utf-8'))
    # print('Exit code:', p.returncode)

    # 父进程创建 Queue, 并传给各个子进程:
    q = Queue()
    pw = Process(target=write, args=(q, ))
    pr = Process(target=read, args=(q, ))
    # 启动子进程 pw, 写入:
    pw.start()
    # 启动子进程 pr, 读取:
    pr.start()
    # 等待 pw 结束
    pw.join()
    # pr 进程里是死循环, 无法等待其结束, 只能强行终止:
    pr.terminate()
