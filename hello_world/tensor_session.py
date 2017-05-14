
import tensorflow as tf

# Define an arbitrary matrix
matrix = tf.constant([[1., 2.]])

# Run the negation operator on it
neg_matrix = tf.neg(matrix)

# Start the session with a special config passed into the constructor to enable
# logging

with tf.Session(config=tf.ConfigProto(log_device_placement=True)) as sess:
    # Tell the session to evaluate negMatrix
    result = sess.run(neg_matrix)

# Print the resulting matrix
print(result)
