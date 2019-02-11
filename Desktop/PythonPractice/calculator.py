#https://github.com/Wakers1/calculator.git
from tkinter import * #Tk, Button, Frame, Entry, Label, INSERT, Text, END
import tkinter.messagebox

def calc():
    """Function to handle the calculation and print answer"""
    number1 = int(num1Entry.get())
    number2 = int(num2Entry.get())
    operator1 = Op1Entry.get()

    try:
        if operator1 == "+":
            answer = (number1 + number2)
        elif operator1 == "-":
            answer = (number1 - number2)
        elif operator1 == "*":
            answer = (number1 * number2)
        elif operator1 == "/":
            answer = (number1 / number2)
        AnsEntry.insert(0.0, answer)
    except ValueError:
        tkinter.messagebox.showwarning("Warning", "Please enter a number.")
    except UnboundLocalError:
        tkinter.messagebox.showwarning("Warning", 'Please enter an Operator, such as "+-*/"')

def clear():
    """Function to clear answer Entry"""
    AnsEntry.delete(0.0, END)


root = Tk()
root.geometry("320x150+400+250")
root.title("Calculator")

lbNum1 = Label(root, text="First Number: ").grid(row=0, column=0)
lbNum2 = Label(root, text="Second Number: ").grid(row=1, column=0)
lbOp1 = Label(root, text="Operator: ").grid(row=2, column=0)
lbAns = Label(root, text="Answer: ").grid(row=3, column=0)

num1Entry = Entry(root, bg="WHITE")
num1Entry.grid(row=0, column =1)
num2Entry = Entry(root, bg="WHITE")
num2Entry.grid(row=1, column =1)
Op1Entry = Entry(root, bg="WHITE")
Op1Entry.grid(row=2, column =1)
AnsEntry = Text(root, width=15, height=1)
AnsEntry.grid(row=3, column =1)

subButton = Button(root, command=calc, text="Submit", width=10).grid(row=4, column=1)
clearButton = Button(root, command=clear, text="Clear", width=10).grid(row=3, column=2)
quitButton = Button(root, command=root.destroy, text="Exit", width=10).grid(row=4, column=2)


root.mainloop()
