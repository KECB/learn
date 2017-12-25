import argparse
import tensorflow as tf


logdir = './graphs/basic_ops/'


def basic_operations():
    a = tf.constant(2, name='a')
    b = tf.constant(3, name='b')
    add = tf.add(a, b, name='add')
    with tf.Session() as sess:
        writer = tf.summary.FileWriter(logdir, sess.graph)
        print(sess.run(add))
        writer.close()


def more_about_constants():
    a = tf.constant([2, 2], name='a')
    b = tf.constant([[0, 1], [2, 3]], name='b')
    x = tf.add(a, b, name='add')
    y = tf.multiply(a, b, name='mul')
    with tf.Session() as sess:
        writer = tf.summary.FileWriter(logdir=logdir, graph=sess.graph)
        x, y = sess.run([x, y])
        print(x, y)
        writer.close()


def tensor_zeros():
    x = tf.zeros([2, 3], tf.int32)
    print(x)
    y = tf.zeros_like(x, optimize=True)
    print(y)
    print(tf.get_default_graph().as_graph_def())
    with tf.Session() as sess:
        y = sess.run(y)
        print(y)


def generator():
    print('*' * 75)
    print('line space')
    with tf.Session() as sess:
        print(sess.run(tf.lin_space(10.0, 13.0, 4)))

    print('*' * 75)
    print('range')
    with tf.Session() as sess:
        print(sess.run(tf.range(3, limit=18, delta=3)))
        print(sess.run(tf.range(5)))

    print('*' * 75)
    print('random')
    with tf.Session() as sess:
        print(sess.run(tf.truncated_normal([3, 3], mean=0.0)))


def operators():
    a = [3, 6]
    b = [2, 2]
    add = tf.add(a, b)
    add_n = tf.add_n([a, b, b])
    mul = tf.multiply(a, b)
    # mat_mul_error = tf.matmul(a, b)
    mat_mul = tf.matmul(tf.reshape(a, [1, 2]), tf.reshape(b, [2, 1]))
    divide = tf.div(a, b)
    mod = tf.mod(a, b)
    with tf.Session() as sess:
        print('tf.add(a, b): {}'.format(sess.run(add)))
        print('tf.add_n([a, b, b]): {}'.format(sess.run(add_n)))
        print('tf.multiply(a, b): {}'.format(sess.run(mul)))
        # print('tf.matmul(a, b): {}'.format(sess.run(mat_mul_error)))
        print('tf.matmul(tf.reshape(a, [1,2]), tf.reshape(b, [2,1])): {'
              '}'.format(sess.run(mat_mul)))
        print('tf.div(a, b): {}'.format(sess.run(divide)))
        print('tf.mod(a, b): {}'.format(sess.run(mod)))


def variable_ops():
    """
    Variable 的 assign 方法会先执行 initilizer，所以不需要先初始化再执行 assign 方法。
    但是 assign_add / assign_sub 必须要先执行初始化方法 initilizer。
    :return:
    """
    print('*' * 75)
    print('initializer')
    w = tf.Variable(tf.truncated_normal([784, 10]))
    with tf.Session() as sess:
        sess.run(w.initializer)
        print(w.eval())

    print('*' * 75)
    print('assign')
    w = tf.Variable(10)
    w.assign(100)
    with tf.Session() as sess:
        sess.run(w.initializer)
        print(w.eval())
        sess.run(w.assign(100))
        print(w.eval())

    print('*' * 75)
    print('assign ops')
    my_var = tf.Variable(2, name='my_var')
    # my_var_time_two 是个Operation Tensor
    my_var_times_two = my_var.assign(my_var * 2)
    with tf.Session() as sess:
        sess.run(my_var.initializer)
        print('my var = {}'.format(my_var.eval()))
        sess.run(my_var_times_two)
        print('my var = {}'.format(my_var.eval()))
        sess.run(my_var_times_two)
        print('my var = {}'.format(my_var.eval()))

    print('*' * 75)
    print('assign add and substract')
    my_var = tf.Variable(10)
    with tf.Session() as sess:
        sess.run(my_var.initializer)
        sess.run(my_var.assign_add(10))
        print('10 + 10 = {}'.format(my_var.eval()))
        sess.run(my_var.assign_sub(4))
        print('10 + 10 - 4 = {}'.format(my_var.eval()))

    print('*' * 75)
    print('each session maintains its own copy of variable')
    w = tf.Variable(10)
    sess1 = tf.Session()
    sess2 = tf.Session()
    sess1.run(w.initializer)
    sess2.run(w.initializer)
    print('sess1 10 + 10 = {}'.format(sess1.run(w.assign_add(10))))
    print('sess2 10 - 2 = {}'.format(sess2.run(w.assign_sub(2))))
    print('sess1 10 + 10 + 100 = {}'.format(sess1.run(w.assign_add(100))))
    print('sess2 10 - 2 - 50 = {}'.format(sess2.run(w.assign_sub(50))))
    sess1.close()
    sess2.close()

    print('*' * 75)
    print('init variable before its value is used to init another variable')
    a = tf.Variable(2)
    # 注意这里最好使用initialized_value方法 避免报错
    b = tf.Variable(2 * a.initialized_value())
    with tf.Session() as sess:
        sess.run(b.initializer)
        print(b.eval())

    print('*' * 75)
    print('interactive session')
    sess = tf.InteractiveSession()
    a = tf.constant(5.0)
    b = tf.constant(6.0)
    c = a * b
    print(c.eval())
    sess.close()


def placeholder():
    print('*' * 75)
    print('basic placeholder')
    a = tf.placeholder(tf.float32, shape=[3])
    b = tf.constant([5, 5, 5], tf.float32)
    c = a + b
    with tf.Session() as sess:
        writer = tf.summary.FileWriter(logdir=logdir, graph=sess.graph,
                                       filename_suffix='placeholder')
        print(sess.run(c, feed_dict={a: [1, 2, 3]}))
        writer.close()

    print('*' * 75)
    print('replace tensor ops with value')
    # tf.Graph.is_feedable(tensor=) 返回 True 则可以使用 feeddict 替代
    a = tf.add(2, 5)
    b = tf.multiply(a, 3)
    with tf.Session() as sess:
        replcae_feed = {a: 15}
        print(sess.run(b, replcae_feed))


def lazyloading():
    x = tf.Variable(10, name='x')
    y = tf.Variable(20, name='y')
    # add = tf.add(x, y)

    # with tf.Session() as sess:
    #     sess.run(tf.global_variables_initializer())
    #     writer = tf.summary.FileWriter(logdir=logdir, graph=sess.graph)
    #     for _ in range(10):
    #         sess.run(add)
    #     writer.close()

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        writer = tf.summary.FileWriter(logdir=logdir, graph=sess.graph)
        for _ in range(10):
            sess.run(tf.add(x, y))
        print(tf.get_default_graph().as_graph_def())
        writer.close()


commmands = {
    'basic_ops': basic_operations,
    'constants': more_about_constants,
    'tensor_zeros': tensor_zeros,
    'generator': generator,
    'operators': operators,
    'variable': variable_ops,
    'placeholder': placeholder,
    'lazyloading': lazyloading
}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--method', help='Method Name')
    args = parser.parse_args()
    if args.method in commmands:
        func = commmands[args.method]
        func()
    else:
        print('Command not found')
