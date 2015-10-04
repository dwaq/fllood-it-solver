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
# the color of the box at (0,0)
origin_color = colors_array[0][0]
for x in range(num_high):
	for y in range(num_wide):
		# first row only cares about what's to the left of it
		if (x == 0):
			# if this is the same color as the origin
			if colors_array[x][y] == origin_color:
				# store a '1' signifying that this color is touching
				touching_array[origin_color][x][y] = 1
			else:
				# once they don't match, stop looking
				break
		# other rows need to match the row abocve it
		else:
			# if this color is the same color as the origin
			if (colors_array[x][y] == origin_color):
				# AND the one above it is "touching"
				if (colors_array[x][y] == touching_array[origin_color][x-1][y]):
					# store a '1' signifying that this color is touching
					touching_array[origin_color][x][y] = 1
				


# draw a small black square on them so I know it's been counted - for debugging
# create columns
#for col in range(num_high):
for col in range(num_high):
    # create a row across in that column
    for row in range(num_wide):
    	if (touching_array[origin_color][col][row] == 1):
    		# if it's touching, color it black
        	c.create_rectangle(row*w, col*h, (row*w)+(w/2), (col*h)+(h/2), fill="black")



mainloop()

# stops crashing when closed
def quit():
    root.destroy()
