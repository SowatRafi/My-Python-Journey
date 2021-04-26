from logging import root
from tkinter import *
from tkinter import ttk
from tkinter import font
import datetime

import txt as txt

global endTime


def quit():
    root.destroy()


def count_wait():
    # Get the time remaining until the event
    time_left = endTime - datetime.datetime.now()
    time_left = time_left - datetime.timedelta(microseconds=time_left.microseconds)
    # remove the microseconds part
    txt.set(time_left)
    # Trigger the countdown after 1000ms
    root.after(1000, count_wait)


# Use tkinter lib for showing the clock
root = Tk()
root.attributes("-fullscree", False)
root.configure(background="green")
root.bind("Quit", quit)
root.after(1000, count_wait)

# Set the end date and time for the countdown
endTime = datetime.datetime(2021, 4, 28, 15, 0, 0)

fnt = font.Font(family="Helvetics", size=60, weight="bold")
txt = StringVar()
lbl = ttk.Label(root, textvariable=txt, font=fnt, foreground="black", background="green")
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
