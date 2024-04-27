# 19. Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Given the head of a linked list, remove the nth node from the end of the list and return its head.

 
# Example 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# Example 2:
# Input: head = [1], n = 1
# Output: []

# Example 3:
# Input: head = [1,2], n = 1
# Output: [1]
 

# Constraints:
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz

# Follow up: Could you do this in one pass?

from ast import List
import collections
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class RemoveNthNodeFromEndLL:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        # create the dummy node and put to the begining of list
        dummy = ListNode(-1, head)

        # create two pointers left and right assign left to dummy node and right to head
        left = dummy
        right = head

        # use two pointers to reach to the (n + 1)th node from end of list -> denoted by left pointer
        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        # delete the nth node by assigning left.next to left.next.next
        left.next = left.next.next

        return dummy.next
    
    def traveseList(self, head: Optional[ListNode]) -> None:
        listStr = ""
        while head:
             if head.next:
                   listStr += (str(head.val) + "->")
             else:
                   listStr += str(head.val)
             head = head.next
        print(listStr)

# Complexity:
# T: O(N)
# S: O(1)

# Testing:
instance = RemoveNthNodeFromEndLL()
head = [1,2,3,4,5]
n = 2
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next, node2.next, node3.next, node4.next = node2, node3, node4, node5
print("Given List:")
print(instance.traveseList(node1))
print("List after removal of", n,"elment:")
print(instance.traveseList(instance.removeNthFromEnd(node1, n)))