import random
import time
import queue
from multiprocessing.managers import BaseManager


# 发送任务的队列:
task_queue = queue.Queue()
# 接收结果的队列:
result_queue = queue.Queue()


# 从 BaseManager 继承的 QueueManager
class QueueManager(BaseManager):
    pass

# 把两个 Queue 都注册到网络上, callable 参数关联了 Queue 对象:
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)
# 绑定端口5000, 设置验证码' abc':
manager = QueueManager(address=('', 5000), authkey=b'abc')
# 启动 Queue
manager.start()
# 获得通过网络访问的 Queue 对象:
task = manager.get_task_queue()
result = manager.get_result_queue()
# 放几个任务进去:
for i in range(10):
    n = random.randrange(0, 10000)
    print('Put task %d...' % n)
    task.put(n)
# 从 result 队列读取结果:
print('Try get result...')
for i in range(10):
    r = result.get(timeout=10)
    print('Result: %s' % r)
# 关闭:
manager.shutdown()
print('master exit.')
