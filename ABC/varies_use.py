import tensorflow as tf

x = tf.Variable([1,2])
a = tf.constant([3,3])
#减法op
SUB = tf.subtract(x,a)
#加法op
ADD = tf.add(x,SUB)

init = tf.global_variables_initializer() #用来初始化变量的一个脚本

with tf.Session() as sess:
    sess.run(init)
    print("SUB:" , sess.run(SUB))
    print("ADD:" , sess.run(ADD))

#创建一个变量初始化为0
state = tf.Variable(0,name='counter')
#创建一个op,作用是state加一
new_value = tf.add(state,1)
#赋值
update = tf.assign(state,new_value)

init1 = tf.global_variables_initializer() #用来初始化此脚本上面定义的变量

with tf.Session() as sess:
    sess.run(init1)
    print(sess.run(state))
    for _ in range(5):
        sess.run(update)
        print(sess.run(state))