#!/usr/bin/python

from Tkinter import *
import random

master = Tk()

c_width = 1000
c_height = 1000

c = Canvas(master, width=c_width, height=c_height)
c.pack()

# create_rectangle(x0, y0, x1, y1, option, ...)

# let's make it 15x15
num_wide = 15
num_high = 15
w = c_width/num_wide
h = c_height/num_high

# we're gonna use 5 colors that Tkinter supports
#colors = ["red", "green", "blue", "purple", "orange"]
# use less now to make work easier to understand
colors = ["red", "green", "blue"]

# create an array of the colors so we can do work on it
colors_array = [[random.randint(0, len(colors)-1) for x in range(num_wide)] for x in range(num_high)]

# using the array, figure out how big the inital "block" is





# draw the colors out
# create columns
for col in range(num_high):
    # create a row across in that column
    for row in range(num_wide):
        c.create_rectangle(row*w, col*h, (row*w)+w, (col*h)+h, fill=colors[colors_array[col][row]])

mainloop()

# stops crashing when closed
def quit():
    root.destroy()
