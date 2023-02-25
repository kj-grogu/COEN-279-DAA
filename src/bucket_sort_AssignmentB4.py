#!/usr/bin/env python3
# bucket_sort.py
from datetime import datetime
#############################################################################################################
#Assignment Bonus - 4																						#
# Python bonus: Create a large array of integers (100,000) elements between 1 and 10,000.					#
# a. Use bucket sort (10 buckets) in each stage to sort it.													#
# b. Use bucket sort  to sort it one time in the ten buckets then sort each bucket using insertion sort. 	#
# c. Compare the running time and report it. 																#
#																											#																					#
#																											#
#############################################################################################################

from functools import reduce
from math import floor
from insertion_sort import insertion_sort




final_res = []

def bucket_sort_final(arr, pow):
	if(len(arr) < 1 or pow < 1):
		return arr

	reducer = pow * 10;
	noOfBuckets = 10
	buckets = [None] * 10

	for i in range(noOfBuckets):
		buckets[i] = []

	for x in arr:
		bi = floor((x % reducer) / pow)
		buckets[bi].append(x)

	res2 = []
	for i in range(len(buckets)):
		sortedArr = bucket_sort_final(buckets[i], pow / 10)
		res2.append(sortedArr)


	if(len(res2) > 1):
		for x in res2:
			final_res.append(x);



# Testing
if __name__ == "__main__":

	import numpy as np

	# Textbook example.
	input = np.random.randint(1, 10000, size=100000)
	testCase = input.copy()
	# list1 = [6292, 2425, 8375, 4575, 5337, 6290, 2315, 2314, 8475, 8473,4676, 5347]
	start_time = datetime.now()
	bucket_sort_final(input, 1000)
	end_time = datetime.now()
	timeDiff = (end_time - start_time).total_seconds() * 10**3
	print(f"Execution time with 100000 elements {timeDiff:.03f}ms")
	output = []

	for val in final_res:
		if val != None  and len(val) > 0:
			output.append(val)

	res = [x for sublist in output for x in sublist]
	#print(res)

	print(np.array_equal(np.sort(testCase), res))