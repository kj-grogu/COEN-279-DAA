import time
from datetime import datetime
import matplotlib.pyplot as plt
#!/usr/bin/env python3
# insertion_sort.py

# Introduction to Algorithms, Fourth edition
# Linda Xiao

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

def insertion_sort(A, n):
	"""Sort a list or numpy array.

	Argument:
	A -- a list or numpy array
	n -- length of A
	"""

	# Traverse the list or array from index 1 to n-1.
	for i in range(1, n):
		key = A[i]

		# Insert A[i] into the sorted subarray a[0:i].
		# Compare stored key with the already sorted values to its left.
		# Move each item one position to the right until we find the 
		# position for the key or fall off the left end of the list or array.
		j = i - 1
		while j >= 0 and A[j] > key:
			A[j + 1] = A[j]
			j -= 1

		# Insert key at the correct position in the list or array.
		A[j + 1] = key


# Testing
if __name__ == "__main__":

	import numpy as np

	# Repeating terms. 
	list1 = [11, 1, 51, 1, 5, 3, 33, 48, 11, 8]
	list1test = list(list1)
	start_time_small = datetime.now()
	insertion_sort(list1, len(list1))
	end_time_small = datetime.now()
	timeDiff = (end_time_small - start_time_small).total_seconds() * 10**3
	print(f"Execution time with 10 elements {timeDiff:.03f}ms")
	print(list1)
	print(list1 == sorted(list1test))


	# 100 elements in array.
	array2 = np.random.randint(-5000, 5000, size=50)
	array2test = np.copy(array2)
	print("Before sorting: ", end = '')
	print(array2)
	start_time_100 = datetime.now()
	insertion_sort(array2, len(array2))
	end_time_100 = datetime.now()
	timeDiff100 = (end_time_100 - start_time_100).total_seconds() * 10**3
	print(f"Execution time with 100 elements {timeDiff100:.03f}ms")
	print("After sorting: ", end = '')
	print(array2)
	print(np.array_equal(array2, np.sort(array2test)))

	# 1000 elements in array.
	array3 = np.random.randint(-5000, 5000, size=100)
	array3test = np.copy(array3)
	print("Before sorting: ", end = '')
	print(array3)
	start_time_1000 = datetime.now()
	insertion_sort(array3, len(array3))
	end_time_1000 = datetime.now()
	timeDiff1000 = (end_time_1000 - start_time_1000).total_seconds() * 10**3
	print(f"Execution time with 1000 elements {timeDiff1000:.03f}ms")
	print("After sorting: ", end = '')
	print(array3)
	print(np.array_equal(array3, np.sort(array3test)))

	# 10000 elements in array.
	array4 = np.random.randint(-5000, 5000, size=150)
	array4test = np.copy(array4)
	print("Before sorting: ", end = '')
	print(array4)
	start_time_10000 = datetime.now()
	insertion_sort(array4, len(array4))
	end_time_10000 = datetime.now()
	timeDiff10000 = (end_time_10000 - start_time_10000).total_seconds() * 10**3
	print(f"Execution time with 10000 elements {timeDiff10000:.03f}ms")
	print("After sorting: ", end = '')
	print(array4)
	print(np.array_equal(array4, np.sort(array4test)))

	# Large array.
	
	array5 = np.random.randint(-5000, 5000, size=200)
	array5test = np.copy(array5)
	print("Before sorting: ", end = '')
	print(array5)
	start_time_large = datetime.now()
	insertion_sort(array5, len(array5))
	end_time_large = datetime.now()
	timeDiff100000 = (end_time_large - start_time_large).total_seconds() * 10**3
	print(f"Execution time with 100000 elements {timeDiff100000:.03f}ms")
	print("After sorting: ", end = '')
	print(array5)
	print(np.array_equal(array5, np.sort(array5test)))
	
	# X axis parameter:
	listx = [10, 50, 100, 150, 200]
	xaxis = listx

	# Y axis parameter:
	listy = [timeDiff, timeDiff100, timeDiff1000, timeDiff10000, timeDiff100000]
	yaxis = listy

	plt.xlabel("InputSize")
	plt.ylabel("TimeTaken ms")
	plt.title("InputSize vs ExecutionTime")
	plt.plot(xaxis, yaxis, linestyle='--', marker='.', color='b', label='')
	plt.grid(color='c', linestyle='-', linewidth=1)
	plt.annotate(f"{timeDiff:.03f}ms ", (10, timeDiff))
	plt.annotate(f"{timeDiff100:.03f}ms ", (50, timeDiff100))
	plt.annotate(f"{timeDiff1000:.03f}ms ", (100, timeDiff1000))
	plt.annotate(f"{timeDiff10000:.03f}ms ", (150, timeDiff10000))
	plt.annotate(f"{timeDiff100000:.03f}ms ", (200, timeDiff100000))
	
	plt.show()


