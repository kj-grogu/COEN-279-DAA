# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/
# Given the head of a singly linked list, reverse the list, and return the reversed list.


# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Example 2:
# Input: head = [1,2]
# Output: [2,1]

# Example 3:
# Input: head = []
# Output: []
 
# Constraints:
# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000

from collections import Counter, defaultdict, deque
import heapq
from ast import List
from typing import List
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class ReverseLinkedList:
	# Definition for singly-linked list.
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     prev = None
    #     cur = head

    #     while cur:
    #         temp = cur.next
    #         cur.next = prev
    #         prev = cur
    #         cur = temp
    
    #     return prev

# Complexity:
# T: O(N)
# S: O(1)

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        newHead = self.reverseList(head.next)

        head.next.next = head 
        # Meaning -> if head = 4, then head.next.next => 4.next.next => 5.next. So, 5.next = head(4)
        head.next = None
        # Meaning -> if head = 4, then head.next => 4.next. So 4.next = None

        return newHead    

# Complexity:
# T: O(N)
# S: O(N), recursive call stack space.

    def traveseList(self, head: Optional[ListNode]) -> None:
        listStr = ""
        while head:
             if head.next:
                   listStr += (str(head.val) + "->")
             else:
                   listStr += str(head.val)
             head = head.next
        print(listStr)
            

          
    
# Testing:
instance = ReverseLinkedList()
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next, node2.next, node3.next, node4.next = node2, node3, node4, node5
print("Given List: ")
print(instance.traveseList(node1))
print("Reversed List: ")
print(instance.traveseList(instance.reverseList(node1)))





        