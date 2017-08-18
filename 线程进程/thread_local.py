import threading

# 创建全局 thread local 对象
local_school = threading.local()


def process_student():
    # 获取当前线程关联的 student
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))


def process_thread(name):
    # 绑定thread local 的 student
    local_school.student = name
    process_student()

t1 = threading.Thread(target=process_thread, args=('Alice', ), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob', ), name='T-B')
t1.start()
t2.start()
t1.join()
t2.join()
