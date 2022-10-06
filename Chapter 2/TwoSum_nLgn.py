import time



def twoSum(A, target):
	"""Find Sum of two elements from the Array A that equal to the provided target value.
	Argument:
	A -- a list or numpy array
	target -- Target value  
	"""	
	A.sort()
	i = 0
	j = len(A) - 1
	retArr = np.array(range(2))
	while(i<j):
		if A[i] + A[j] < target:
			i+=1
			continue
		if A[i] + A[j] > target:
			j-=1
			continue
		else:
			retArr[0] = A[i]
			retArr[1] = A[j]
			break
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