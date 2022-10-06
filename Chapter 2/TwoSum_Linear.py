import time



def twoSum(A, target):
	"""Find Sum of two elements from the Array A that equal to the provided target value.
	Argument:
	A -- a list or numpy array
	target -- Target value  
	"""
	my_dictionary = {}
	retArr = np.array(range(2))
	for i in range(1, len(A)):
		key = target - A[i]
		if key in my_dictionary.keys():
			retArr[0] = key
			retArr[1] = A[i]
		else:
			my_dictionary[A[i]] = i
	return retArr
		
# Testing
if __name__ == "__main__":
	import numpy as np
	# Repeating terms. 
	A = np.array([11, 1, 51, 1, 5, 3])
	target = 6 
	retArr = np.array(range(2))
	retArr = twoSum(A, target)	
	print(retArr)

