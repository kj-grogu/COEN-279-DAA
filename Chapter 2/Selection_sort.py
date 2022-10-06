class Elements:
	def __init__(self, index, value):
		self.index = index
		self.value = value
	def __repr__(self):
		return f"Index: {self.index} Value: {self.value}"


def Selection_sort(A, n):
	"""Sort a list or numpy array.

	Argument:
	A -- a list or numpy array
	n -- length of A
	"""
	print("Elements to be sorted: ")
	print("Array: ", A)
	listElements = [None] * n
	for i in range(0,n):
		obj = Elements(i, A[i])
		listElements.insert(i,obj)
	
	print("Elements with their index before sorting of their values: ")
	for i in range(0,n):
		print(listElements[i])

	# Traverse the list or array from index 1 to n.
	for i in range(0, n):
		Smallest = listElements[i]
		swapIndex = i
		# Serch the remainder of the array for the smallest element
		for j in range(i+1,n):
			if(listElements[j].value < Smallest.value):
				Smallest = listElements[j]
				swapIndex = j

		# Swap if the smallest element isn't at the current index
		if(i != swapIndex):
			temp = listElements[i]
			listElements[i] = Smallest
			listElements[swapIndex] = temp
			
	print("Elements with their prior index after sorting of their values: ")
	for i in range(0,n):
		print(listElements[i])

# Testing
if __name__ == "__main__":

	import numpy as np

	# Repeating terms. 
	list1 = [4, 2, 3, 4, 1]
	list1test = list(list1)
	Selection_sort(list1, len(list1))
	print("The output above shows that selection sort is not stable as the relative order of the elements with same value is not maintained")
	print("4 with index of 3 comes before the 4 with index of 0")
	

