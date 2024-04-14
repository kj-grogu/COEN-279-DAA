# 274. H-Index
# https://leetcode.com/problems/h-index/
# Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.
# According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

 

# Example 1:
# Input: citations = [3,0,6,1,5]
# Output: 3
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
# Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.

# Example 2:
# Input: citations = [1,3,1]
# Output: 1
 

# Constraints:
# n == citations.length
# 1 <= n <= 5000
# 0 <= citations[i] <= 1000

 # what is h-index, h is some no in list citations such that there at least h papers that have been cited h or more times:
        # meaning: 
        # 1. total no. of papers -> len(citations) = N, 0 to N
        # 2. Citation for each paper i in (0 to N) is the no of citations for this paper = citations[i]
        # 3. Find max value of C where there are C or more papers with C or more citations which is H
        # 4. example:
            # 4.1. citations = [3,0,6,1,5], N = 5
            # 4.2. find C (citations) and P(Papers) vals:
                # 4.2.1. for C1 = 3 or more citations there are P1 = 3 papers(0, 2, 4)
                # 4.2.2. for C2 = 0 or more citations there are P2 = 5 papers(0, 1, 2, 3, 4)
                # 4.2.3. for C3 = 6 or more citations there is P3 = 1 paper(3)
                # 4.2.4. for C4 = 1 or more citations there are P4 = 4 papers(0, 2, 3, 4)
                # 4.2.5. for C5 = 5 or more citations there are P5 = 2 papers(2, 4)
            # 4.3. List all Cs where for which val of P is >= H:
                # 4.3.1 C1(3) -> P1(3), Yes P1 >= C1
                # 4.3.2 C2(0) -> P2(5), Yes P2 >= C2
                # 4.3.1 C3(6) -> P3(1), No P3 not >= C3
                # 4.3.1 C4(1) -> P4(4), No P4 not >= C4 
                # 4.3.1 C5(5) -> P5(2), No P5 not >= C5 
            # 4.4. return the C which is P >= C and with max val: max(C1, C2) -> max(3, 0) -> 3 this is H
    # Explanation doesn't tell how code works, its just to explain the problem

from ast import List
import collections
import heapq
from typing import List
from typing import Optional

class H_Index:
    def hIndex(self, citations: List[int]) -> int:
        totalPapers = len(citations) 
        citationToPaper = [0] * (totalPapers + 1) # Buckets
        
        for c in citations:
            if c > totalPapers:
                citationToPaper[-1] += 1
            else:
                citationToPaper[c] += 1

        # print("citationToPaper ->", citationToPaper)

        sum = 0
        for h in range(len(citationToPaper) - 1, -1, -1):
            sum += citationToPaper[h]

            if sum >= h:
                return h

        return -1

# Complexity:
# T: O(N)
# S: O(N)

# Testing:
instance = H_Index()
citations = [1,3,1]
print("give the paper and their citations: ")
for i, c in enumerate(citations):
    print("Paper", i + 1, "has", c, "citations")
print("H index for the these papers and their citations is: ", instance.hIndex(citations))
# Output: 1


            

        
        

        