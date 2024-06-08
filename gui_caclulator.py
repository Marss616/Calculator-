from tkinter import *
import math

print("the version of Tkinter is...", TkVersion)

root = Tk()
root.title("jacks calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# createing number buttons

def button_click(number):
    current = e.get()
    print(type(current))    
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_click_pi(number):
    current = e.get()
    print(type(current))    
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


# createing other buttons 
def input_button_clear(END):
    e.delete(0, END)

def input_button_equals():
    s_num = e.get()
    
    if math == "addition":
        s_num = e.get()
        s_num = int(s_num)
        e.delete(0, END)
        e.insert(0, f_num + s_num)

    elif math == "subraction":
        s_num = e.get()
        s_num = int(s_num)
        e.delete(0, END)
        e.insert(0, f_num - s_num)

    elif math == "multiplication":
        s_num = e.get()
        s_num = int(s_num)
        e.delete(0, END)
        e.insert(0, f_num * s_num)

    elif math == "division":
        s_num = e.get()
        s_num = int(s_num)
        e.delete(0, END)
        e.insert(0, f_num / s_num)

    elif math == "squareroot":
        answer =  f_num ** 0.5
        e.delete(0, END)
        e.insert(0, answer)

    elif math == "squared":
        answer = f_num * f_num
        e.delete(0, END)
        e.insert(0, answer)

    elif math == "persent":
        s_num = e.get()
        s_num = float(s_num)
        answer = f_num / s_num * 100
        e.delete(0, END)
        e.insert(0, answer)

    elif math == "pi":
        return

    elif math == "x/100":
        return 
        #answer = f_num 1/(100)
        #e.insert(0, answer)

    else:
        print("use the buttons lol")
    
def input_button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number) 
    e.delete(0, END)
    
def input_button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subraction"
    f_num = float(first_number) 
    e.delete(0, END)

def input_button_mulutipy():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number) 
    e.delete(0, END)

def input_button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number) 
    e.delete(0, END)

def input_button_squareroot():
    first_number = e.get()
    global f_num
    global math
    math = "squareroot"
    f_num = float(first_number)
    e.delete(0, END)

def input_button_squared():
    first_number = e.get()
    global f_num
    global math
    math = "squared"
    f_num = float(first_number)
    e.delete(0, END)

def input_button_persent():
    first_number = e.get()
    global f_num
    global math
    math = "persent"
    f_num = float(first_number)
    e.delete(0, END)

def input_button_x1():
    first_number = e.get()
    global f_num
    global math
    math = "x/100"
    f_num = float(first_number)
    e.delete(0, END)


# createing number buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
# createing other buttons
button_clear = Button(root, text="clear", padx=29, pady=20, command= lambda:input_button_clear(END))
button_equals = Button(root, text="=", padx=38, pady=80, command=input_button_equals)
# divstion buttons
button_add = Button(root, text="+", padx=39, pady=20, command=input_button_add)
button_subtract = Button(root, text="-", padx=40, pady=20, command=input_button_subtract)
button_mulutiply = Button(root, text="*", padx=40.5, pady=20, command=input_button_mulutipy)
button_divide = Button(root, text="/", padx=40, pady=20, command=input_button_divide)
# complex buttons
button_squareroot = Button(root, text="√x", padx=38, pady=20, command=input_button_squareroot)
button_squared = Button(root, text="x²", padx=36, pady=20, command=input_button_squared)
button_persent = Button(root, text="%", padx=36, pady=20, command=input_button_persent)
# pi button
button_pi = Button(root, text="π", padx=38, pady=20, command=lambda: button_click(3.141592653589793238462643))
button_x1 = Button(root, text="x/1", padx=33, pady=20, command=input_button_x1)
#exit button
button_quit = Button(root, text="exit",padx=40,pady=40, command=root.quit)

button_quit.grid(row=8,column=8)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_subtract.grid(row=6, column=1)
button_mulutiply.grid(row=6, column=2)
button_add.grid(row=6, column=0)
button_0.grid(row=5, column=1)
button_x1.grid(row=7, column=1)
button_divide.grid(row=6, column=3)
button_clear.grid(row=8, columnspan=3, column=0)
button_squareroot.grid(row=8, column=0)
button_squared.grid(row=8, column=2)
button_persent.grid(row=7, column=2)
button_pi.grid(row=7, column=0)
button_equals.grid(row=6, column=4)

root.mainloop()
