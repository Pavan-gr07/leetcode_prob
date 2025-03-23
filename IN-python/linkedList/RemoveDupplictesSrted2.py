# 82. Remove Duplicates from Sorted List II
# Medium
# Topics
# Companies
# Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

 

# Example 1:


# Input: head = [1,2,3,3,4,4,5]
# Output: [1,2,5]
# Example 2:


# Input: head = [1,1,1,2,3]
# Output: [2,3]
 

# Constraints:

# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head
# Example Usage
if __name__ == "__main__":
    # Create a linked list from a list
    values = [1, 2, 6, 3, 6, 4]
    head = create_linked_list(values)
class Solution:   
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        prev = cur =dummy, head
        while cur and cur.next:
            nextNode = cur.next
            if cur.val == nextNode.val:
                  prev.next = cur.next.next
                  cur = prev.next
            else:
                 prev = cur

            cur = cur.next
        return head
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")
if __name__ == "__main__":
    # Create a linked list from a list
    values = [1, 2, 3, 3, 4, 4]
    head = create_linked_list(values)
    solution = Solution()
    new_head = solution.removeElements(head)
    
    print_linked_list(new_head)