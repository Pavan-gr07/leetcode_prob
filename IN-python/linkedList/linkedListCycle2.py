""" 
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
"""
class Solution:
    #Function to find first node if the linked list has a loop.
    def findFirstNode(self, head):
        #code here
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                pre = head
                while pre != slow:
                    pre = pre.next
                    slow = slow.next
                return pre.data
        return None

