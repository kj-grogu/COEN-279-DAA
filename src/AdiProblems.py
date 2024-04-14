# Q2: Write a Python program to remove a specific digit from every element of the list
# Example:
# Input : test_list = [333, 893, 1948, 34, 2346]
# K = 3
# Output : [”, 89, 1948, 4, 246]
# Explanation : All occurrences of 3 are removed.
# Input : test_list = [345, 893, 1948, 34, 2346],
# K = 5
# Output : [34, 893, 1948, 34, 2346]
# Explanation : All occurrences of 5 are removed.
 
# [ ]
# ### Python Q2: Write Code here

class RemoveDigit:
	def removeSpecificDegit(self, nums: list[list[int]], digit: int) -> list[list[str]]:
		res = []
		for num in nums:
			strNum = str(num)
			curNum = ""
			for d in strNum:
				if int(d) != digit:
					curNum += d
			res.append(curNum)
		return res
# Testing:
instance = RemoveDigit()
nums = [333, 893, 1948, 34, 2346]
K = 3
print("################################Solution Q2#################################")
print("nums list after removal of digit", K, "from ", nums, "is: ", instance.removeSpecificDegit(nums,K))


# Q3: Write a Python program to Check Common Letters in Two Input Strings
# e.g.
# str1="springer"
# str2="nature"
# output: the common letters "nre" (sequence doesn't matter)
 
# [ ]
# ### Python Q3: Write Code here

class CommonLetters:
	def findCommonLetters(self, str1: str, str2: str) -> str:
		charSet = set(str1)
		res = ""
		for c in str2:
			if c in charSet:
				res += c

		return res

# Testing:
instance = CommonLetters()
str1="springer"
str2="nature"
print("################################Solution Q3#################################")
print("Common Letters in \"", str1, "\" and \"", str2, "\" are:", instance.findCommonLetters(str1, str2))
		

