import tkinter

def button1_command():
    print('Button 1 default command.')

def print_hello(event):
    #print(event.char)
    #print(event.keycode)
    print(event.num)
    print(event.x, event.y)
    #print(event.x_root, event.y_root)
    me = event.widget
    # Что делать с me?
    if me == button1:
        print('Hello!')
    elif me == button2:
        print('You pressed button2!')
    else:
        raise ValueError()


def inint_main_window():
    """
    Инициализация главного окна: создание всех необходимых виджетов и их упаковка.
    :return:
    """
    global root, button1, button2, label, text,scale

    root = tkinter.Tk()

    button1 = tkinter.Button(root, text="Button 1", command=button1_command)
    button1.bind("<Button>",print_hello)


    button2 = tkinter.Button(root, text="Button 2")
    button2.bind("<Button>",print_hello)

    varible = tkinter.IntVar()
    label = tkinter.Label(root, text='Some text.')
    scale = tkinter.Scale(root)
    text = tkinter.Entry(root)

    for obj in button1, button2, label, scale, text:
      obj.pack()


if __name__== "_main__":
    init_main_window()

    root.mainloop()