# 138. Copy List with Random Pointer
# https://leetcode.com/problems/copy-list-with-random-pointer/

# A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

# Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, 
# where each new node has its value set to the value of its corresponding original node. 
# Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list 
# and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

# For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

# Return the head of the copied linked list.

# The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
# Your code will only be given the head of the original linked list.

# Example 1:
# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

# Example 2:
# Input: head = [[1,1],[2,1]]
# Output: [[1,1],[2,1]]

# Example 3:
# Input: head = [[3,null],[3,0],[3,null]]
# Output: [[3,null],[3,0],[3,null]]

# Constraints:
# 0 <= n <= 1000
# -104 <= Node.val <= 104
# Node.random is null or is pointing to some node in the linked list.

from ast import List
from typing import List
from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class CopyLLWithRandomPtr:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        copy_map = {}
        copy_map[head] = Node(head.val)
        placeholder = head

        while head:
            if head.next and head.next not in copy_map:
                copy_map[head.next] = Node(head.next.val)
            
            copy_map[head].next = copy_map.get(head.next, None) 
            
            if head.random and head.random not in copy_map:
                copy_map[head.random] = Node(head.random.val)
                
            copy_map[head].random = copy_map.get(head.random, None)

            head = head.next
        
        return copy_map[placeholder]
    
    def traveseList(self, head: Optional[Node]) -> None:
        cur = head
        listStrNext = ""
        listStrRandom = ""
        while head:
             if head.next:
                   listStrNext += (str(head.val) + "->")
             else:
                   listStrNext += str(head.val) 
             head = head.next
        
        while cur:
             if cur.random:
                 listStrRandom += (str(cur.val) + "->" + str(cur.random.val) + ":")
             else:
                 listStrRandom += (str(cur.val) + ":")
             cur = cur.next
        print("Next list:",listStrNext)
        print("Random List:",listStrRandom)

# Complexity:
# T: O(N)
# S: O(N)
    
# Testing:
        
# Testing:
instance = CopyLLWithRandomPtr()
node1 = Node(7)
node2 = Node(13)
node3 = Node(11)
node4 = Node(10)
node5 = Node(1)
node1.next, node2.next, node3.next, node4.next = node2, node3, node4, node5
node1.random, node2.random, node3.random, node4.random, node5.random = None, node1, node5, node3, node1
print("Given List: ")
print(instance.traveseList(node1))
print("Reversed List:")
print(instance.traveseList(instance.copyRandomList(node1)))
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

    

        