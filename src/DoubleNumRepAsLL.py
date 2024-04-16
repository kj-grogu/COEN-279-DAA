# 2816. Double a Number Represented as a Linked List
# https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/

# You are given the head of a non-empty linked list representing a non-negative integer without leading zeroes.

# Return the head of the linked list after doubling it.

# Example 1:
# Input: head = [1,8,9]
# Output: [3,7,8]
# Explanation: The figure above corresponds to the given linked list which represents the number 189. 
# Hence, the returned linked list represents the number 189 * 2 = 378.

# Example 2:
# Input: head = [9,9,9]
# Output: [1,9,9,8]
# Explanation: The figure above corresponds to the given linked list which represents the number 999. 
# Hence, the returned linked list reprersents the number 999 * 2 = 1998. 

# Constraints:
# The number of nodes in the list is in the range [1, 104]
# 0 <= Node.val <= 9
# The input is generated such that the list represents a number that does not have leading zeros, 
# except the number 0 itself.


from typing import Optional
from ast import List
import collections
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Logic:
# 1. reverse the given linked list
# 2. Iterate over the reversed list and calulate prod, cur.val and carry
# 3. in case of last node if there is carry, create new node with carry as val 
# and put as next node for current node and don't forget to break
# 4. Reverse and return this new product list

class DoubleNumRepAsLL:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = self.reverse(head)
        # print(cur)
        carry = 0
        res = cur
        while cur:
            prod = (cur.val * 2) + carry
            cur.val = prod % 10
            carry = prod // 10
            if not cur.next and carry:
                cur.next = ListNode(carry, None)
                break
            
            cur = cur.next
        
        return self.reverse(res)


    def reverse(self, head):
        prev = None
        cur = head

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        return prev
    
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
instance = DoubleNumRepAsLL()
node1 = ListNode(1)
node2 = ListNode(8)
node3 = ListNode(9, None)

node1.next, node2.next = node2, node3
print("Given List: ")
print(instance.traveseList(node1))
print("Doubled List: ")
print(instance.traveseList(instance.doubleIt(node1)))

