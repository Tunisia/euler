#!/usr/bin/python

#Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#
#
#
#How many such routes are there through a 20x20 grid?

size = 20

a = math.factorial(size*2)/(math.factorial(size)**2)
print a