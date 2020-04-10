import tensorflow as tf
print(tf.__version__)


A = tf.constant([[1.0, 2.0], [3.0, 4.0]])
B = tf.constant([[1.0, 1.0], [0.0, 1.0]])
print(A)
print(B)
C = tf.matmul(A, B)
print(C)





# Previously we would have to create Sessions to solve these kind of problems,
# But now its done automatically -> EAGER EXECUTIONS

# OLD Approaches with Session
# Kind of Deprecated

# session = tf.compat.v1.Session()
# print(session.run(C)
