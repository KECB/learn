from multiprocessing import Process
import os


# 子进程要执行的代码
def run_proc(name, count):
    print('Run child process %s %s (%s)...' % (name, count, os.getpid()))

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test', '1', ))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')
