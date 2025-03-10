# 234. Palindrome Linked List
# Solved
# Easy
# Topics
# Companies
# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

 

# Example 1:


# Input: head = [1,2,2,1]
# Output: true
# Example 2:


# Input: head = [1,2]
# Output: false



from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Base case: if head is None, return None
        if not head:
            return None
        
        # Recursive call for the next node
        head.next = self.removeElements(head.next, val)
        
        # If current node's value matches val, skip it
        return head.next if head.val == val else head

# Helper function to create a linked list from a list
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print the linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example Usage
if __name__ == "__main__":
    # Create a linked list from a list
    values = [1, 2, 6, 3, 6, 4]
    head = create_linked_list(values)
    
    print("Original Linked List:")
    print_linked_list(head)
    
    # Remove elements with value 6
    val_to_remove = 6
    solution = Solution()
    new_head = solution.removeElements(head, val_to_remove)
    
    print("\nLinked List after removing", val_to_remove, ":")
    print_linked_list(new_head)
