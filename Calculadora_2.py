from tkinter import *


def concatenation(event):
    global value_text
    global value
    global sinal

    value_text += sinal + value
    text_var.set(value_text)


def reset():
    global value_text
    value_text = ''


def input_value(event):
    global value_text
    global value
    global sinal

    if len(value_text) == 0:
        if event in '*/-+':
            text_var.set(value_text)

    elif value_text[-1] in '*/-=' and event not in '*/-+':
        ...


def output_value():
    eval(value_text)
    text_var.set(value_text)


# colors:
color1 = '#252526' # Cinza
color2 = '#090d3a' # Azul
color3 = '#fff7f7' # Branco
color4 = '#e5a97b' # Laranja
color5 = '#000000' # Preto

window = Tk()
window.geometry('362x459')
window.config(background=color3)

frame_tela = Frame(window, width=362, height=100, background=color2)
frame_tela.grid(column=0, row=0)

frame_functions = Frame(window, width=362, height=359, background=color5)
frame_functions.grid(column=0, row=1)

# Text:
text_var = StringVar()
text = Label(frame_tela, height=2, width=10, background=color2, textvariable=text_var, fg=color3, anchor='e', font='Ivy 25', padx=160, pady=20)
text.place(x=0, y=0)

# Result:
value_text: str = ''
value = ''
sinal = ''

# Button:
button_clear = Button(frame_functions, width=17, height=3, fg=color5, background=color4, command=reset, font='Ivy 12 bold', text='C', relief=RAISED, overrelief=RIDGE)
button_clear.place(x=0, y=0)

button_modulo = Button(frame_functions, width=8, height=3, fg=color5, background=color4, command=lambda: input_value('%'), font='Ivy 12 bold', text='%', relief=RAISED, overrelief=RIDGE)
button_modulo.place(x=181, y=0)

button_multiplicacao = Button(frame_functions, width=8, height=3, fg=color5, background=color4, command=lambda: input_value('*'), font='Ivy 12 bold', text='*', relief=RAISED, overrelief=RIDGE)
button_multiplicacao.place(x=272, y=0)

button_9 = Button(frame_functions, width=8, height=3, fg=color5, background=color3, command=lambda: input_value('9'), font='Ivy 12 bold', text='9', relief=RAISED, overrelief=RIDGE)
button_9.place(x=0, y=72)

button_8 = Button(frame_functions, width=8, height=3, fg=color5, background=color3, command=lambda: input_value('8'), font='Ivy 12 bold', text='8', relief=RAISED, overrelief=RIDGE)
button_8.place(x=90, y=72)

button_7 = Button(frame_functions, width=8, height=3, fg=color5, background=color3, command=lambda: input_value('7'), font='Ivy 12 bold', text='7', relief=RAISED, overrelief=RIDGE)
button_7.place(x=181, y=72)

button_divisao = Button(frame_functions, width=8, height=3, fg=color5, background=color4, command=lambda: input_value('/'), font='Ivy 12 bold', text='/', relief=RAISED, overrelief=RIDGE)
button_divisao.place(x=272, y=72)

button_6 = Button(frame_functions, width=8, height=3, fg=color5, background=color3, command=lambda: input_value('6'), font='Ivy 12 bold', text='6', relief=RAISED, overrelief=RIDGE)
button_6.place(x=0, y=144)

button_5 = Button(frame_functions, width=8, height=3, fg=color5, background=color3, command=lambda: input_value('5'), font='Ivy 12 bold', text='5', relief=RAISED, overrelief=RIDGE)
button_5.place(x=90, y=144)

button_4 = Button(frame_functions, width=8, height=3, fg=color5, background=color3, command=lambda: input_value('4'), font='Ivy 12 bold', text='4', relief=RAISED, overrelief=RIDGE)
button_4.place(x=181, y=144)

button_adicao = Button(frame_functions, width=8, height=3, fg=color5, background=color4, command=lambda: input_value('+'), font='Ivy 12 bold', text='+', relief=RAISED, overrelief=RIDGE)
button_adicao.place(x=272, y=144)

button_3 = Button(frame_functions, width=8, height=3, fg=color5, background=color3, command=lambda: input_value('3'), font='Ivy 12 bold', text='3', relief=RAISED, overrelief=RIDGE)
button_3.place(x=0, y=216)

button_2 = Button(frame_functions, width=8, height=3, fg=color5, background=color3, command=lambda: input_value('2'), font='Ivy 12 bold', text='2', relief=RAISED, overrelief=RIDGE)
button_2.place(x=90, y=216)

button_1 = Button(frame_functions, width=8, height=3, fg=color5, background=color3, command=lambda: input_value('1'), font='Ivy 12 bold', text='1', relief=RAISED, overrelief=RIDGE)
button_1.place(x=181, y=216)

button_subtracao = Button(frame_functions, width=8, height=3, fg=color5, background=color4, command=lambda: input_value('-'), font='Ivy 12 bold', text='-', relief=RAISED, overrelief=RIDGE)
button_subtracao.place(x=272, y=216)

button_0 = Button(frame_functions, width=17, height=3, fg=color5, background=color3, command=lambda: input_value('0'), font='Ivy 12 bold', text='0', relief=RAISED, overrelief=RIDGE)
button_0.place(x=0, y=288)

button_dot = Button(frame_functions, width=8, height=3, fg=color5, background=color3, command=lambda: input_value('.'), font='Ivy 12 bold', text='.', relief=RAISED, overrelief=RIDGE)
button_dot.place(x=181, y=288)

button_igual = Button(frame_functions, width=8, height=3, fg=color5, background=color4, command=lambda: input_value('='), font='Ivy 12 bold', text='=', relief=RAISED, overrelief=RIDGE)
button_igual.place(x=272, y=288)

mainloop()
