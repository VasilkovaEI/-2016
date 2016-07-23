from drawman import *
from time import sleep

A = [(0,0), (100, 0), (100,100), (0, 100)]

for x, y in A:
    pen_down()
    to_point(x, y)
to_point (A[0][0], A [0] [1])
pen_up()

sleep(20)


