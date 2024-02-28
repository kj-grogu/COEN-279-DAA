# 143. Reorder List
# https://leetcode.com/problems/reorder-list/

# You are given the head of a singly linked-list. The list can be represented as:
# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

# Example 1:
# Input: head = [1,2,3,4]
# Output: [1,4,2,3]

# Example 2:
# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]
 

# Constraints:
# The number of nodes in the list is in the range [1, 5 * 104].
# 1 <= Node.val <= 1000

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

class ReorderList:
    def traveseList(self, head: Optional[ListNode]) -> None:
          listStr = ""
          while head:
              if head.next:
                   listStr += (str(head.val) + "->")
              else:
                   listStr += str(head.val)
              head = head.next
          print(listStr)

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return None

        # find middle of list:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next

        # reverse the 2nd half of the list:
        slow.next = prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # merge the two list one node from 1st and next node from second and so on:
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2

        return head

# Complexity:
# T: O(N)
# S: O(1)

	

# Testing:
instance = ReorderList()
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next, node2.next, node3.next, node4.next = node2, node3, node4, node5
print("Given List: ")
print(instance.traveseList(node1))
print("Reordered List: ")
print(instance.traveseList(instance.reorderList(node1)))

        