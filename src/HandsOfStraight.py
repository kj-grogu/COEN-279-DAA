from ast import List
import heapq
from typing import List
from typing import Optional

# 846. Hand of Straights
# https://leetcode.com/problems/hand-of-straights/
# Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

# Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.

 

# Example 1:
# Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
# Output: true
# Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]

# Example 2:
# Input: hand = [1,2,3,4,5], groupSize = 4
# Output: false
# Explanation: Alice's hand can not be rearranged into groups of 4.

class HandsOfStraight:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        count = {}
        for num in hand:
            count[num] = 1 + count.get(num, 0)

        minHeap = list(count.keys())
        heapq.heapify(minHeap)

        while minHeap:
            first = minHeap[0]

            for i in range(first, first + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)

        return True

# Complexity:
# T: O(N + M log M) where N is length of hand and M is the no. of unique elements in list hand
# S: O(M) for count and minHeap

# Testing
instance = HandsOfStraight()
hand = [1,2,3,6,2,3,4,7,8]
groupSize = 3

print("Can create hands of straight with all elements of hand ", hand, " list with groupSize ", groupSize, " :", instance.isNStraightHand(hand, groupSize))
        