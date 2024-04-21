# 160. Intersection of Two Linked Lists
# https://leetcode.com/problems/intersection-of-two-linked-lists/

# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. 
# If the two linked lists have no intersection at all, return null.
# For example, the following two linked lists begin to intersect at node c1:
# The test cases are generated such that there are no cycles anywhere in the entire linked structure.
# Note that the linked lists must retain their original structure after the function returns.

# Custom Judge:
# The inputs to the judge are given as follows (your program is not given these inputs):
# intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
# listA - The first linked list.
# listB - The second linked list.
# skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
# skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
# The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your program. 
# If you correctly return the intersected node, then your solution will be accepted.


# Example 1:
# Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
# Output: Intersected at '8'
# Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
# From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; 
# There are 3 nodes before the intersected node in B.
# - Note that the intersected node's value is not 1 because the nodes with value 1 in A and B (2nd node in A and 3rd node in B) are different node references. 
# In other words, they point to two different locations in memory, while the nodes with value 8 in A and B (3rd node in A and 4th node in B) point to the same location in memory.

# Example 2:
# Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
# Output: Intersected at '2'
# Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
# From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; 
# There are 1 node before the intersected node in B.

# Example 3:
# Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
# Output: No intersection
# Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, 
# intersectVal must be 0, while skipA and skipB can be arbitrary values.
# Explanation: The two lists do not intersect, so return null.
 

# Constraints:
# The number of nodes of listA is in the m.
# The number of nodes of listB is in the n.
# 1 <= m, n <= 3 * 104
# 1 <= Node.val <= 105
# 0 <= skipA < m
# 0 <= skipB < n
# intersectVal is 0 if listA and listB do not intersect.
# intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.

# Follow up: Could you write a solution that runs in O(m + n) time and use only O(1) memory?

# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class IntersectionOfTwoLL:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # step1: find the length of 2 lists:
        lenA = lenB = 0

        curA, curB = headA, headB
        while curA:
            lenA += 1
            curA = curA.next
        
        while curB:
            lenB += 1
            curB = curB.next

        # step2: move the longer list ahead to make it same length as other
        if lenA > lenB:
            for i in range(lenA - lenB):
                headA = headA.next
        elif lenB > lenA:
            for i in range(lenB - lenA):
                headB = headB.next
        
        # step3: move both list pointers ahead until they reach intersection point then return
        while headA:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next

        return None  

    def traveseList(self, head: Optional[ListNode]) -> None:
        listStr = ""
        while head:
             if head.next:
                   listStr += (str(head.val) + "->")
             else:
                   listStr += str(head.val)
             head = head.next
        print(listStr)     

# complexity:
# Time Complexity: O(N + M)
# Space Complexity: O(1)
    
# Testing:
instance = IntersectionOfTwoLL()
node1 = ListNode(4)
node2 = ListNode(1)
node3 = ListNode(8)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next, node2.next, node3.next, node4.next = node2, node3, node4, node5
headA = node1
node6 = ListNode(5)
node7 = ListNode(6)
node6.next, node7.next = node7, node2
headB = node6
print("The two given lists are:")
print("List 1:")
instance.traveseList(headA)
print("List 2:") 
instance.traveseList(headB)
print("Node of intersection for the two lists is:", instance.getIntersectionNode(headA, headB).val)
# Output: Intersected at '1'