#https://github.com/Wakers1/calculator.git
from tkinter import * #EXCEPTION, Tk, Button, Frame, Entry, Label, INSERT, Text, END
import tkinter.messagebox

def calc():
    """Function to handle the calculation and print answer"""
    number1 = int(num1Entry.get())
    number2 = int(num2Entry.get())
    operator1 = Op1Entry.get()
    AnsEntry.delete(0.0, END)
    try:
        if operator1 == "+":
            answer = (number1 + number2)
        elif operator1 == "-":
            answer = (number1 - number2)
        elif operator1 == "*":
            answer = (number1 * number2)
        elif operator1 == "/":
            answer = (number1 / number2)
        elif operator1 == "%": # Modulus
            answer = (number1 % number2)
        elif operator1 == "**": # Exponent
            answer = (number1 ** number2)
        elif operator1 == "//": # Floor devision
            answer = (number1 // number2)
        AnsEntry.insert(0.0, answer)
        """Exceptions to be captured for bad input"""
    except Exception as e:
        tkinter.messagebox.showerror("Warning", e)
    except TypeError:
        tkinter.messagebox.showwarning("Warning", "Please enter a number.")
    except ValueError:
        tkinter.messagebox.showwarning("Warning", "Please enter a number.")
    except UnboundLocalError:
        tkinter.messagebox.showwarning("Warning", 'Please enter an Operator, such as "+-*/"')

def clear():
    """Function to clear answer Entry"""
    AnsEntry.delete(0.0, END)
    num1Entry.delete(0, END)
    num2Entry.delete(0, END)
    Op1Entry.delete(0, END)

root = Tk()
root.geometry("320x150+400+250") # 320x330 for button option
root.title("Calculator")

"""Labels for the GUI"""
lbNum1 = Label(root, text="First Number: ").grid(row=0, column=0)
lbNum2 = Label(root, text="Second Number: ").grid(row=1, column=0)
lbOp1 = Label(root, text="Operator: ").grid(row=2, column=0)
lbAns = Label(root, text="Answer: ").grid(row=3, column=0)

"""Entry boxes for user input"""
num1Entry = Entry(root, bg="WHITE")
num1Entry.grid(row=0, column =1)
num2Entry = Entry(root, bg="WHITE")
num2Entry.grid(row=1, column =1)
Op1Entry = Entry(root, bg="WHITE")
Op1Entry.grid(row=2, column =1)
AnsEntry = Text(root, width=15, height=1)
AnsEntry.grid(row=3, column =1)
opHint = Label(root, text="eg. + - *", fg="GREY")
opHint.grid(row=2, column=2)

""" Submit, Clear and Quit buttons for GUI"""
subButton = Button(root, command=calc, text="Submit", width=10).grid(row=4, column=1)
clearButton = Button(root, command=clear, text="Clear", width=10).grid(row=3, column=2)
quitButton = Button(root, command=root.destroy, text="Exit", width=10).grid(row=4, column=2)

# """Includes individual button options"""
# oneButton = Button(root, text="1", width=10).grid(row=5, column=0)
# twoButton = Button(root, text="2", width=10).grid(row=5, column=1)
# threeButton = Button(root, text="3", width=10).grid(row=5, column=2)
# fourButton = Button(root, text="4", width=10).grid(row=6, column=0)
# fiveButton = Button(root, text="5", width=10).grid(row=6, column=1)
# sixButton = Button(root, text="6", width=10).grid(row=6, column=2)
# sevenButton = Button(root, text="7", width=10).grid(row=7, column=0)
# eightButton = Button(root, text="8", width=10).grid(row=7, column=1)
# nineButton = Button(root, text="9", width=10).grid(row=7, column=2)
# zeroButton = Button(root, text="0", width=10).grid(row=8, column=1)
# clear2Button = Button(root, text="Clear", width=10).grid(row=8, column=0)
# sub2Button = Button(root, text="Submit", width=10).grid(row=8, column=2)

root.mainloop()


