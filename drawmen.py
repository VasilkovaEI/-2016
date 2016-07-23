from turtle import Turtle


def init_drawman():
    global t, x_current, y_current, drawmen_scale
    t = Turtle()
    t.penup()
    x_current = 0
    y_current = 0
    t.goto(x_current, y_current)
    drawmen_scale = 10


def test_drawman():
    """
    Тестирование работы Чертёжника
    :return: None
    """
    pen_down()
    for i in range(5):
        on_vector(10, 20)
        on_vector(10, -20)
    pen_up()
    to_point(0,0)

init_drawman()
def pen_down():
    t.pendown()


def pen_up():
    t.penup()


def on_vector(dx,dy):
    to_point(x_cyrrent + dx, y_current + dy)


def to_point (x,y):
    global x_current, y_current
    x_current = x
    y_current = y
    t.goto(drawmen_scale*x_current,drawmen_scale*y_current)

init_drawman()
if __name__== '__main__':
    import time
    test_drawman()
    time.sleep(10)