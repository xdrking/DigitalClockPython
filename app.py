# importing module
from tkinter import *
from time import *
from time import strftime
import tkinter as tk

# creating tkinter window
root = tk.Tk()
root.title('Python Clock 1.0')

root.geometry('420x120')

root.resizable(width=False, height=False)


# This function is used to 
# display time on the label
def clock():
    text = strftime('%H.%M.%S')
    label.config(text=text)
    label.after(1000,clock)
    

label = Label(root,font=("ds-digital",100),background="black",foreground="yellow")
label.pack(fill=BOTH, expand=True,anchor='n') 

clock()

mainloop()  



 