import datetime
from logging import root
from tkinter import *
from tkinter import font
from tkinter import ttk

import txt as txt


def quit():
    root.destroy()


def clock_time():
    time = datetime.datetime.now()
    time = (time.strftime("%Y - %m - %d\n%H : %M : %S"))
    # time = (time.strftime("%H %M %S"))

    txt.set(time)
    root.after(1000, clock_time)


root = Tk()
root.attributes("-fullscree", False)
root.configure(background="black")
root.bind("x", quit)
root.after(1000, clock_time)

fnt = font.Font(family="Helvetics", size=60, weight="bold")
txt = StringVar()
lbl = ttk.Label(root, textvariable=txt, font=fnt, foreground="white", background="black")
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
