#!/usr/bin/env python3
# bucket_sort.py

# Introduction to Algorithms, Fourth edition
# Linda Xiao
from datetime import datetime
#########################################################################
#                                                                       #
# Copyright 2022 Massachusetts Institute of Technology                  #
#                                                                       #
# Permission is hereby granted, free of charge, to any person obtaining #
# a copy of this software and associated documentation files (the       #
# "Software"), to deal in the Software without restriction, including   #
# without limitation the rights to use, copy, modify, merge, publish,   #
# distribute, sublicense, and/or sell copies of the Software, and to    #
# permit persons to whom the Software is furnished to do so, subject to #
# the following conditions:                                             #
#                                                                       #
# The above copyright notice and this permission notice shall be        #
# included in all copies or substantial portions of the Software.       #
#                                                                       #
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,       #
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF    #
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND                 #
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS   #
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN    #
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN     #
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE      #
# SOFTWARE.                                                             #
#                                                                       #
#########################################################################

from math import floor
from insertion_sort import insertion_sort


def bucket_sort(A, n):
	"""Sort an array or list of n elements distributed uniformly over [0, 1).
	
	Argument:
	A -- an array/list
	n -- length of A

	Returns:
	A sorted list 
	"""
	# Make B a list of n empty lists.
	B = [None] * 10
	for i in range(10):
		B[i] = []

	# Distribute the n input numbers into n equal-sized subintervals
	for i in range(n):
		B[floor(A[i]/1000)].append(A[i])

	# Sort each subinterval. 
	for i in range(10):
		insertion_sort(B[i], len(B[i]))

	# Concatenate the lists b[0], b[1], ...b[n-1] together in order.
	return [x for sublist in B for x in sublist]


# Testing
if __name__ == "__main__":

	import numpy as np

	array5 = np.random.randint(1,10000, size=100000)
	array5test = np.copy(array5)
	print("Before sorting: ", end = '')
	print(array5)
	start_time = datetime.now()
	array5 = bucket_sort(array5, len(array5))
	end_time = datetime.now()
	timeDiff = (end_time - start_time).total_seconds() * 10**3
	print(f"Execution time with 100000 elements {timeDiff:.03f}ms")
	print("After sorting: ", end = '')
	#print(array5)
	print(np.array_equal(np.sort(array5test), array5))
