import tensorflow as tf

t = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9], [2, 3, 4]])

sess = tf.Session()
print sess.run(tf.shape(t))
print sess.run(tf.size(t))
print sess.run(tf.rank(t))
