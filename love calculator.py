from tkinter import *
import random
root = Tk()
root.geometry('400x400')
root.title('love calculator')
def calculate_love():
    st = '6789'
    digit = 2
    temp = "".join(random.sample(st, digit))
    result.config(text=temp)

heading = Label(root, text="love calculator")
heading.pack()

slot1 = Label(root, text="Enter your name")
slot1.pack()
name1 = Entry(root, border=5)
name1.pack()

slot2 = Label(root, text="Enter your Partner name")
slot2.pack()
name2 = Entry(root, border=5)
name2.pack()

bt = Button(root, text="calculate", height=1, width=7, command=calculate_love)
bt.pack()

result = Label(root, text="love persantage between both of you")
result.pack()
root.mainloop()
