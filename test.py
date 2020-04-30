import tensorflow as tf

print(tf.__version__)

initializer = tf.initializers.GlorotUniform()
trans = tf.Variable(initializer(shape=(10, 10)), name="transition")

print(trans)

