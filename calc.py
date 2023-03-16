import tkinter
from tkinter import *

root = Tk()
root.title("Calculator Hamid")
root.geometry("350x570")
root.resizable(False, False)
root.configure(bg="#ffffff")
FONT = ("Anomoly ", 20)
equation = ""


def show(value):
    global equation
    operators = ['+', '-', '*', '/', '.']  # daftar operator yang diizinkan
    if equation == "" and value in operators:  # operator tidak boleh ditekan jika belum ada bilangan
        return
    # operator tidak boleh ditekan lebih dari satu kali berturut-turut
    if equation[-1:] in operators and value in operators:
        return
    equation += value
    label_result.config(text=equation)


def clear():
    global equation
    equation = ""
    label_result.config(text=equation)


def delete_one():
    global equation
    equation = equation[:-1]
    label_result.config(text=equation)


def percent():
    global equation
    if equation != "":
        try:
            value = eval(equation)
            value = value / 100
            equation = str(value)
            label_result.config(text=equation)
        except:
            equation = "error"
            label_result.config(text=equation)


def plus_minus():
    global equation
    if equation != "":
        try:
            value = eval(equation)
            value = -1 * value
            equation = str(value)
            label_result.config(text=equation)
        except:
            equation = "error"
            label_result.config(text=equation)


def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result = eval(equation)
        except:
            result = "error"
            equation = ""
    label_result.config(text=result)


label_result = Label(root, width=23, height=2, text="",
                     font=("Anomoly ", 20), bg="#ECF2FF", fg="#000000")
label_result.pack()

Button(root, text="C", width=3, height=1,  font=("Anomoly ", 20), bd=0,
       fg="#F2921D", bg="#ffffff", command=lambda: clear()).place(x=10, y=100)
Button(root, text="\u232b", width=3, height=1,  font=("Anomoly ", 20), bd=0,
       fg="#F2921D", bg="#ffffff", command=lambda: delete_one()).place(x=100, y=100)
Button(root, text="%", width=3, height=1,  font=("Anomoly ", 20), bd=0,
       fg="#F2921D", bg="#ffffff", command=lambda: percent()).place(x=190, y=100)
Button(root, text="x", width=3, height=1,  font=("Anomoly ", 20), bd=0,
       fg="#F2921D", bg="#ffffff", command=lambda: show("*")).place(x=280, y=100)

Button(root, text="7", width=3, height=1,  font=("Anomoly ", 20), bd=0,
       fg="#000000", bg="#ffffff", command=lambda: show("7")).place(x=10, y=200)
Button(root, text="8", width=3, height=1,  font=("Anomoly ", 20), bd=0,
       fg="#000000", bg="#ffffff", command=lambda: show("8")).place(x=100, y=200)
Button(root, text="9", width=3, height=1,  font=("Anomoly ", 20), bd=0,
       fg="#000000", bg="#ffffff", command=lambda: show("9")).place(x=190, y=200)
Button(root, text="-", width=3, height=1,  font=("Anomoly ", 20), bd=0,
       fg="#F2921D", bg="#ffffff", command=lambda: show("-")).place(x=280, y=200)

Button(root, text="4", width=3, height=1,  font=("Anomoly ", 20), bd=0,
       fg="#000000", bg="#ffffff", command=lambda: show("4")).place(x=10, y=300)
Button(root, text="5", width=3, height=1,  font=("Anomoly ", 20), bd=0,
       fg="#000000", bg="#ffffff", command=lambda: show("5")).place(x=100, y=300)
Button(root, text="6", width=3, height=1,  font=("Anomoly ", 20), bd=0,
       fg="#000000", bg="#ffffff", command=lambda: show("6")).place(x=190, y=300)
Button(root, text="+", width=3, height=1,  font=("Anomoly ", 20), bd=0,
       fg="#F2921D", bg="#ffffff", command=lambda: show("+")).place(x=280, y=300)

Button(root, text="1", width=3, height=1,  font=("Anomoly ", 20), bd=0,
       fg="#000000", bg="#ffffff", command=lambda: show("1")).place(x=10, y=400)
Button(root, text="2", width=3, height=1,  font=("Anomoly ", 20), bd=0,
       fg="#000000", bg="#ffffff", command=lambda: show("2")).place(x=100, y=400)
Button(root, text="3", width=3, height=1,  font=("Anomoly ", 20), bd=0,
       fg="#000000", bg="#ffffff", command=lambda: show("3")).place(x=190, y=400)
Button(root, text="/", width=3, height=1,  font=("Anomoly ", 20), bd=0,
       fg="#F2921D", bg="#ffffff", command=lambda: show("/")).place(x=280, y=400)

Button(root, text="+/-", width=3, height=1,  font=("Anomoly ", 20), bd=0,
       fg="#F2921D", bg="#ffffff", command=lambda: plus_minus()).place(x=10, y=500)
Button(root, text="0", width=3, height=1,  font=("Anomoly ", 20), bd=0,
       fg="#000000", bg="#ffffff", command=lambda: show("0")).place(x=100, y=500)
Button(root, text=".", width=3, height=1,  font=("Anomoly ", 20), bd=0,
       fg="#000000", bg="#ffffff", command=lambda: show(".")).place(x=190, y=500)
Button(root, text="=", width=3, height=1,  font=("Anomoly ", 20), bd=0,
       fg="#fff", bg="#F2921D", command=lambda: calculate()).place(x=280, y=500)

root.mainloop()
