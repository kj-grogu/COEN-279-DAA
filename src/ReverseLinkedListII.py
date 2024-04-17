# 92. Reverse Linked List II
# https://leetcode.com/problems/reverse-linked-list-ii/
# Given the head of a singly linked list and two integers left and right where left <= right, 
# reverse the nodes of the list from position left to position right, and return the reversed list.

# Example 1:
# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]

# Example 2:
# Input: head = [5], left = 1, right = 1
# Output: [5]

# Constraints:
# The number of nodes in the list is n.
# 1 <= n <= 500
# -500 <= Node.val <= 500
# 1 <= left <= right <= n
 
# Follow up: Could you do it in one pass?

from ast import List
import collections
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class ReverseLinkedListII:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        # Step 1: Reach a node previous to left node, so we can keep track of start pointer to reversed list
        leftPrev, cur = dummy, head
        for _ in range(left - 1):
            leftPrev = cur
            cur = cur.next
        # Now leftPrev points to a node prior to left position and cur to left position
        
        # Step 2: Reverse the nodes from left to right position:
        prev = None
        for _ in range(right - left + 1):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        # Now prev is head of reversed node, cur points to the next node to right position

        # Step 3: Now join the list as reversed list is not connected
        # currently: leftPrev.next points to left node which is now the end of reversed list 
        leftPrev.next.next = cur
        leftPrev.next = prev
        
        # return head of new list denoted by dummy.next
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
instance = ReverseLinkedListII()
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
left = 2
right = 4
node1.next, node2.next, node3.next, node4.next = node2, node3, node4, node5
print("Given List:")
print(instance.traveseList(node1))
print("Reversed List II:")
print(instance.traveseList(instance.reverseBetween(node1, left, right)))

# Output: [1,4,3,2,5]










            

        

        