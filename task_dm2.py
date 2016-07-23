from drawmen import *
from time import sleep

def f(x):
    return x*x

pen_down()
for x in range(0,11):
    to_point(x, f(x))
to_point (A[0][0], A [0] [1])
pen_up()

sleep(10)

