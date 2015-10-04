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
colors = ["red", "green"]

# create an array of the colors so we can do work on it
colors_array = [[random.randint(0, len(colors)-1) for x in range(num_wide)] for x in range(num_high)]

# draw the colors out
# create columns
for col in range(num_high):
    # create a row across in that column
    for row in range(num_wide):
        c.create_rectangle(row*w, col*h, (row*w)+w, (col*h)+h, fill=colors[colors_array[col][row]])


#print colors_array[0]

# keep track of what colors are touching in a giant array
touching_array = [[[0 for x in range(num_wide)] for x in range(num_high)] for x in range(len(colors))]

#print touching_array


# using the array, figure out how big the inital "block" is
# go across row 0, seeing how far it's the same color
y_cntr = 0
# the color of the box at (0,0)
origin_color = colors_array[0][0]
for y in range(num_wide):
	# if this is the same color as the origin, increase counter
	if colors_array[0][y] == origin_color:
		y_cntr = y_cntr+1;
	else:
		# once they don't match, stop looking
		break

print y_cntr



# draw a small black square on them so I know it's been counted - for debugging
# create columns
#for col in range(num_high):
for col in range(1):
    # create a row across in that column
    for row in range(y_cntr):
        c.create_rectangle(row*w, col*h, (row*w)+(w/2), (col*h)+(h/2), fill="black")



mainloop()

# stops crashing when closed
def quit():
    root.destroy()
