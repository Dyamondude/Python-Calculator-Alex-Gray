# Alex Gray
# 15/09/22

# ***************************************************
# Python Calculator with GUI (Graphic User Interface)
# ***************************************************

from tkinter import * # import the tkinter library

def button_press(num):  # defining each button press
    global equation_text

    equation_text = equation_text + str(num)

    equation_label.set(equation_text)



def equals():
    global equation_text

    try:  # try is used in try...except blocks. It defines a block of code test if it contains any errors.
          # You can define different blocks for different error types, and blocks to execute if nothing went wrong.
        total = str(eval(equation_text)) # Parases the expression argument and evaluates it as a python expression.

        equation_label.set(total)

        equation_text = total

    except SyntaxError: # Check for syntax error

        equation_text.set("SYNTAX ERROR")

        equation_text = ""

    except ZeroDivisionError:  # Check for division by zero

        equation_label.set("ARITHMETIC ERROR")

        equation_text = ""


def clear():  # Clears the equation_label for the next calculation
    global equation_text

    equation_label.set("")

    equation_text = ""




# Designing the user interface

window = Tk()  # tou can use window, root, ... or a descriptive variable of your own
window.title("Calculator Program")  # Title in the window bar
window.geometry("500x550")  # size of the window dependant on your design
window.configure(bg ="grey19")  # Window colour dependant on your design

equation_text = ""  # Starting off with no text in the label

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=("console", 20), bg = "#A5BD81", width=24, height=3)
label.pack()  # widgets have to be "pack"ed into the window

frame = Frame(window)
frame.pack()

# creating number buttons

button1 = Button(frame, text=1, height=4, width=9, font=35, bg = "grey49", command=lambda: button_press(1))
button1.grid(row=0, column=0) 

button2 = Button(frame, text=2, height=4, width=9, font=35, bg = "grey49", command=lambda: button_press(2))
button2.grid(row=0, column=1) 

button3 = Button(frame, text=3, height=4, width=9, font=35, bg = "grey49", command=lambda: button_press(3))
button3.grid(row=0, column=2) 

button4 = Button(frame, text=4, height=4, width=9, font=35, bg = "grey49", command=lambda: button_press(4))
button4.grid(row=1, column=0) 

button5 = Button(frame, text=5, height=4, width=9, font=35, bg = "grey49", command=lambda: button_press(5))
button5.grid(row=1, column=1) 

button6 = Button(frame, text=6, height=4, width=9, font=35, bg = "grey49", command=lambda: button_press(6))
button6.grid(row=1, column=2) 

button7 = Button(frame, text=7, height=4, width=9, font=35,bg = "grey49", command=lambda: button_press(7))
button7.grid(row=2, column=0) 

button8 = Button(frame, text=8, height=4, width=9, font=35, bg = "grey49", command=lambda: button_press(8))
button8.grid(row=2, column=1) 

button9 = Button(frame, text=9, height=4, width=9, font=35, bg = "grey49", command=lambda: button_press(9))
button9.grid(row=2, column=2) 

button0 = Button(frame, text=0, height=4, width=9, font=35,bg = "grey49", command=lambda: button_press(0))
button0.grid(row=3, column=0) 

# Create operation buttons

plus = Button(frame, text='+', height=4, width=9, font=35,bg = "grey49", command=lambda: button_press('+'))
plus.grid(row=0, column=3) 

minus = Button(frame, text='-', height=4, width=9, font=35, bg = "grey49", command=lambda: button_press('-'))
minus.grid(row=1, column=3) 

multiply = Button(frame, text='×', height=4, width=9, font=35,bg = "grey49", command=lambda: button_press('*'))
multiply.grid(row=2, column=3) 

divide = Button(frame, text='÷', height=4, width=9, font=35,bg = "grey49", command=lambda: button_press('/'))
divide.grid(row=3, column=3) 

# create equals

equal = Button(frame, text='=', height=4, width=9, font=35,bg = "grey49", command=equals)
equal.grid(row=3, column=2) 

# create decimal

decimal = Button(frame, text='.', height=4, width=9, font=35, bg = "grey49", command=lambda: button_press('.'))
decimal.grid(row=3, column=1) 

# create clear button

clear = Button(window, text='clear', height=4, width=19, font=35, bg = "grey49", command=clear)
clear.pack()



window.mainloop()