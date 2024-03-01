# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/
# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
 
# Constraints:
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.


from collections import Counter, defaultdict, deque
import heapq
from ast import List
from typing import List
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class AddTwoNumsLL:
    def traveseList(self, head: Optional[ListNode]) -> None:
         listStr = ""
         while head:
              if head.next:
                   listStr += (str(head.val) + "->")
              else:
                   listStr += str(head.val)
              head = head.next
         print(listStr)
        
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return None
        elif not l1 or not l2:
            return l1 or l2
        else:
            carry = 0
            res = ListNode(0)
            sentinel = res

            while l1 or l2:
                l1_val = l1.val if l1 else 0
                l2_val = l2.val if l2 else 0

                curr_sum = l1_val + l2_val + carry
                carry = curr_sum // 10
                res.next = ListNode(curr_sum % 10)
                res = res.next

                l1 = l1.next if l1 else None
                l2 = l2.next if l2 else None

            if carry:
                res.next = ListNode(carry)

            return sentinel.next

# Complexity:
# T:O(N + M), N len of l1 and M len of l2
# S:O(N + M), N len of l1 and M len of l2
        
# Testing:
instance = AddTwoNumsLL()
node1 = ListNode(9)
node2 = ListNode(9)
node3 = ListNode(9)
node4 = ListNode(9)
node5 = ListNode(9)
node6 = ListNode(9)
node7 = ListNode(9)
node1.next, node2.next, node3.next, node4.next, node5.next, node6.next, node7.next = node2, node3, node4, node5, node6, node7, None
l1 = node1

node8 = ListNode(9)
node9 = ListNode(9)
node10 = ListNode(9)
node11 = ListNode(9)
node8.next, node9.next, node10.next, node11.next = node9, node10, node11, None
l2 = node8

print("Add the  nos from the two lists provided below: ")
print("List 1: ", instance.traveseList(l1))
print("List 2: ", instance.traveseList(l2))

print("The sum of nums from above two lists is: ")
print(instance.traveseList(instance.addTwoNumbers(l1,l2)))

        


        