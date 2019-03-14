from __future__ import print_function
import tensorflow as tf
from utils.vocab import Vocabulary


'''def t_yeild():
    ct = 1
    a, b = [1, 1], 0
    while ct < 10:
        a += [1, 1]
        b -= 1
        ct += 1
        yield a, b

for i in t_yeild():
    print(i)
c = tf.cast(t_yeild(), dtype=tf.float32)
ending = tf.strided_slice(c, [0, 0], [9, -1], [1, 1])
print(ending)
'''
def debug():
    import inspect
    caller_name = inspect.stack()[1][3]
    print ("[DEBUG]: enter {}()".format(caller_name))

def say_hello():
    debug()
    print ("hello!")

def say_goodbye():
    debug()
    print ("goodbye!")

if __name__ == '__main__':
    say_hello()
    say_goodbye()