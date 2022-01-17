# Python program to print nXn
# chessboard pattern using numpy

import numpy as np

# function to print Chessboard pattern
def printchessboard(n):
	
	print("Chessboard pattern:")

	# create a n * n matrix
	x = np.zeros((n, n), dtype = int)

	# fill with 1 the alternate rows and columns
	x[1::2, ::2] = 1
	x[::2, 1::2] = 1
	
	# print the pattern
	for i in range(n):
		for j in range(n):
			print(x[i][j], end =" ")
		print()


# driver code
n = 8
printchessboard(n)
