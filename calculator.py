import tkinter as tk
from tkinter import ttk

def is_valid_input(text, input):
    if text[-1] in ['+','-','*','/'] and input in ['+','-','*','/']:
        return False
    if text[-1] in ['+','-','*','/'] and (input == '0' or input == '='):
        return False
    return True
    
def button_input(value):
    if not is_valid_input(calc_display['text'], value):
        return False

    if calc_display['text'] == '0':
        calc_display['text'] = value
    else:
        calc_display['text'] += value

def calculate():
    if not is_valid_input(calc_display['text'], '='):
        return False
    display_text = calc_display['text']
    calc_display['text'] = str(eval(display_text))

def clear_display():
    calc_display['text'] = '0'

root = tk.Tk()
root.title("Calculator")
root.resizable(False, False)
root.geometry("315x300")

frame = ttk.Frame(root)
frame['padding'] = (10, 10)

frame2 = ttk.Frame(root)
frame2['padding'] = (10, 10)

frame3 = ttk.Frame(root)
frame3['padding'] = (10, 10)

frame.grid(column=0, row=0)
frame2.grid(column=0, row=1)
frame3.grid(column=0, row=2)

calc_display = tk.Label(frame, text="0", bg="white")
calc_display.grid(column=0, row=0, columnspan=4, sticky=tk.W, ipadx=5, ipady=5)

btn_1 = ttk.Button(frame2, text="1", command=lambda: button_input('1'))
btn_1.grid(column=0, row=0, padx=(0,5), pady=(0,5))

btn_2 = ttk.Button(frame2, text="2", command=lambda: button_input('2'))
btn_2.grid(column=1, row=0, padx=(0,5), pady=(0,5))

btn_3 = ttk.Button(frame2, text="3", command=lambda: button_input('3'))
btn_3.grid(column=2, row=0, padx=(0,5), pady=(0,5))

btn_4 = ttk.Button(frame2, text="4", command=lambda: button_input('4'))
btn_4.grid(column=0, row=1, padx=(0,5), pady=(0,5))

btn_5 = ttk.Button(frame2, text="5", command=lambda: button_input('5'))
btn_5.grid(column=1, row=1, padx=(0,5), pady=(0,5))

btn_6 = ttk.Button(frame2, text="6", command=lambda: button_input('6'))
btn_6.grid(column=2, row=1, padx=(0,5), pady=(0,5))

btn_7 = ttk.Button(frame2, text="7", command=lambda: button_input('7'))
btn_7.grid(column=0, row=2, padx=(0,5), pady=(0,5))

btn_8 = ttk.Button(frame2, text="8", command=lambda: button_input('8'))
btn_8.grid(column=1, row=2, padx=(0,5), pady=(0,5))

btn_9 = ttk.Button(frame2, text="9", command=lambda: button_input('9'))
btn_9.grid(column=2, row=2, padx=(0,5), pady=(0,5))

btn_0 = ttk.Button(frame2, text="0", command=lambda: button_input('0'))
btn_0.grid(column=1, row=3, padx=(0,5), pady=(0,5))

btn_add = ttk.Button(frame3, text="+", command=lambda: button_input('+'))
btn_add.grid(column=0, row=0, padx=(0,5), pady=(0,5))

btn_subtract = ttk.Button(frame3, text="-", command=lambda: button_input('-'))
btn_subtract.grid(column=1, row=0, padx=(0,5), pady=(0,5))

btn_multiply = ttk.Button(frame3, text="x", command=lambda: button_input('*'))
btn_multiply.grid(column=2, row=0, padx=(0,5), pady=(0,5))

btn_divide = ttk.Button(frame3, text="÷", command=lambda: button_input('/'))
btn_divide.grid(column=0, row=1, padx=(0,5), pady=(0,5))

btn_equal = ttk.Button(frame3, text="=", command=calculate)
btn_equal.grid(column=1, row=1, padx=(0,5), pady=(0,5))

btn_clear = ttk.Button(frame3, text="AC", command=clear_display)
btn_clear.grid(column=2, row=1, padx=(0,5), pady=(0,5))

root.mainloop()