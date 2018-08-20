import tensorflow as tf

#创建一个一行两列的常量矩阵
m1 = tf.constant([[3,3]])
#创建一个两行一列的常量矩阵
m2 = tf.constant([[2],[3]])
#创建一个矩阵乘法op
product = tf.matmul(m1,m2)
print(product) #product是一个tensor对象

#定义一个会话
sess = tf.Session()
#调用会话的run方法进行矩阵乘法
result = sess.run(product)
print(result)
sess.close()
#也可用 with tf.Session() as sess