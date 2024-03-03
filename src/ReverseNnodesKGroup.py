# 25. Reverse Nodes in k-Group
# https://leetcode.com/problems/reverse-nodes-in-k-group/
# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

# You may not alter the values in the list's nodes, only nodes themselves may be changed.

# Example 1:
# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]

# Example 2:
# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]
 

# Constraints:
# The number of nodes in the list is n.
# 1 <= k <= n <= 5000
# 0 <= Node.val <= 1000
 
# Follow-up: Can you solve the problem in O(1) extra memory space?


from collections import Counter, defaultdict, deque
import heapq
from ast import List
from typing import List
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class ReverseNnodesKGroups:
    def traveseList(self, head: Optional[ListNode]) -> None:
        listStr = ""
        while head:
             if head.next:
                   listStr += (str(head.val) + "->")
             else:
                   listStr += str(head.val)
             head = head.next
        print(listStr)
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        # Node that keeps track of the last node of the most recenlt reversed group of nodes, 
        # to make it point to the first node of next group to be reversed
        groupPrev = dummy

        while True:
            # To get the last node of current group
            kth = self.getKth(groupPrev, k)
            if not kth:
                break # Meaning we don't have enough nodes to form a group of k, so no reversal needed
            
            # To keep track of first node of next group
            groupNext = kth.next

            # Logic to reverse the group of k nodes:
            # prev = kth.next because prev needs have the node that the curr will point to while reversing
            # as we can't keep it None, so we make it point to the curr's next node that should now come after curr node
            # That is in case of -1 -> 2 -> 1 -> 3 -> 4 -> 5
            # here kth = 4th, groupPrev = 1. So, prev = 4th.next (Kth.next) = 5 and curr = 3 and curr.next = 3.next = 4
            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # Now put kth at the begining of the reversed group pointed by the group previous i-e becoming next of the previous group
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp
     
        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

# Complexity:
# T: O(2N) = O(N)
# S: O(1)

# Testing:
# Example 1:
# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]
instance = ReveseNnodesKGroups()
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next, node2.next, node3.next, node4.next = node2, node3, node4, node5
print("Given List: ")
print(instance.traveseList(node1))
k = 2
print("Given grouping size: ", k)
print("Reversed List: ")
print(instance.traveseList(instance.reverseKGroup(node1, k)))
    
       



        