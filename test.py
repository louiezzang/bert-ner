import tensorflow as tf

print(tf.__version__)

initializer = tf.initializers.GlorotUniform()
trans = tf.Variable(initializer(shape=(10, 10)), name="transition")

print(trans)

@tf.function
def simple_nn_layer(x, y):
    return tf.nn.relu(tf.matmul(x, y))


x = tf.random.uniform((3, 3))
y = tf.random.uniform((3, 3))

simple_nn_layer(x, y)

