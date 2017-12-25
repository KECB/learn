import tensorflow as tf
import sys
import argparse


def part1():
    a = tf.constant(2, name='a')
    b = tf.constant(3, name='b')
    x = tf.add(a, b, name='add')
    with tf.Session() as sess:
        writer = tf.summary.FileWriter('./graphs', sess.graph)
        print(sess.run(x))
    writer.close()


def part2():
    x = 2
    y = 3
    op1 = tf.add(x, y)
    op2 = tf.multiply(x, y)
    op3 = tf.pow(op1, op2)

    with tf.Session() as sess:
        writer = tf.summary.FileWriter('./graphs', sess.graph)


def subgraphs():
    x = 2
    y = 3
    add_op = tf.add(x, y)
    mul_op = tf.multiply(x, y)
    useless = tf.multiply(x, add_op)
    pow_op = tf.pow(add_op, mul_op)
    with tf.Session() as sess:
        writer = tf.summary.FileWriter('./graphs', sess.graph)
        z, not_useless = sess.run([pow_op, useless])
        print(z)
        print(not_useless)
    writer.close()


def multigraphs():
    g1 = tf.get_default_graph()
    g2 = tf.Graph()
    # add ops to the default graph
    with g1.as_default():
        a = tf.constant(3)
    # add ops to the user created graph
    with g2.as_default():
        b = tf.constant(5)
    sess = tf.Session(graph=g1)
    writer = tf.summary.FileWriter('./graphs', sess.graph,
                                   filename_suffix='g1')
    writer.close()
    sess.run(a)

    sess = tf.Session(graph=g2)
    writer = tf.summary.FileWriter('./graphs', sess.graph,
                                   filename_suffix='g2')
    writer.close()
    sess.run(b)
    

commands = {
    'part1': part1,
    'part2': part2,
    'subgraphs': subgraphs,
    'multiG': multigraphs
}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-m', '--method', help='Method name')
    args = parser.parse_args()
    if args.method in commands:
        func = commands[args.method]
        func()
    else:
        print('command not found')
    # if args.method == 'part1':
    #     print('part1')
    #     part1()
    # if args.method == 'part2':
    #     print('part2')
    #     part2()

