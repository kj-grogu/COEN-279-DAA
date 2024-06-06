# 1268. Search Suggestions System
# https://leetcode.com/problems/search-suggestions-system/

# logic video:
# https://www.youtube.com/watch?v=D4T2N0yAr20

# You are given an array of strings products and a string searchWord.
# Design a system that suggests at most three product names from products after each character of searchWord is typed. 
# Suggested products should have common prefix with searchWord. 
# If there are more than three products with a common prefix return the three lexicographically minimums products.
# Return a list of lists of the suggested products after each character of searchWord is typed.

# Example 1:
# Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
# Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
# Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"].
# After typing m and mo all products match and we show user ["mobile","moneypot","monitor"].
# After typing mou, mous and mouse the system suggests ["mouse","mousepad"].

# Example 2:
# Input: products = ["havana"], searchWord = "havana"
# Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
# Explanation: The only word "havana" will be always suggested while typing the search word. 

# Constraints:
# 1 <= products.length <= 1000
# 1 <= products[i].length <= 3000
# 1 <= sum(products[i].length) <= 2 * 104
# All the strings of products are unique.
# products[i] consists of lowercase English letters.
# 1 <= searchWord.length <= 1000
# searchWord consists of lowercase English letters.

from typing import List


class SearchSuggestionsSystem:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # Initialize the result list to store suggestions after each character of searchWord is typed
        res = []

        # Sort the products lexicographically
        products.sort()

        # Initialize pointers for the range of relevant products
        l, r = 0, len(products) - 1

        # Iterate through each character in the searchWord
        for i in range(len(searchWord)):
            c = searchWord[i]  # Current character to match

            # Narrow down the left pointer if the current product does not match the prefix
            while l <= r and (len(products[l]) <= i or products[l][i] != c):
                l += 1

            # Narrow down the right pointer if the current product does not match the prefix
            while l <= r and (len(products[r]) <= i or products[r][i] != c):
                r -= 1

            # Initialize the current suggestion list for this character
            res.append([])

            # Calculate the number of remaining products that match the prefix
            remain = r - l + 1

            # Append at most 3 lexicographically smallest products to the suggestion list
            for j in range(min(3, remain)):
                res[-1].append(products[l + j])

        # Return the list of suggestions for each character in searchWord
        return res

# Complexity:
# Time Complexity: O(N log N + M * N), where N is the number of products and M is the length of the searchWord.
# - Sorting the products takes O(N log N).
# - For each character in the searchWord (M characters), we may scan through all products (N products), hence O(M * N).

# Space Complexity: O(N), where N is the number of products.
# - The sorted list of products takes O(N) space.
# - The result list res can have up to M sublists, but each sublist will contain at most 3 products, which is constant space relative to N.
    
# Testing:
instance = SearchSuggestionsSystem()
products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"

print("Given list of products is:", products)
print("Given word to conduct the search based on:", searchWord)
print("List of suggested product row-wise where every row represents list of suggested products after matching the rowth char of search word:")
res = instance.suggestedProducts(products, searchWord)
for i in range(len(res)):
    print(res[i])

# Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]


