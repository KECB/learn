import threading
import multiprocessing

def loop():
    x = 0
    while True:
        x = x ^ 1

# cpu占用只能达到102%, 原因是python 解释器执行代码时有一个 GIL(Global Interpreter Lock)
# 锁, 也就是说 python 只能用到1核, 要想多核运行, 需要重写解释器. 如需要实现多核执行, 需要使用
# 多进程来实现.
# Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。多线程的并发在Python中就是一个
# 美丽的梦。
for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()

