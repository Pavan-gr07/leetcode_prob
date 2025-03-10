# 148. Sort List
# Medium
# Topics
# Companies
# Given the head of a linked list, return the list after sorting it in ascending order.

 

# Example 1:


# Input: head = [4,2,1,3]
# Output: [1,2,3,4]
# Example 2:


# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]
# Example 3:

# Input: head = []
# Output: []
 

# Constraints:

# The number of nodes in the list is in the range [0, 5 * 104].
# -105 <= Node.val <= 105
 

# Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?


# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 978.1K
# Submissions
# 1.6M
# Acceptance Rate
# 60.9%



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # Base case: if head is None or there's only one element, return head
        if not head or not head.next:
            return head

        # Step 1: Split the list into two halves
        mid = self.getMiddle(head)
        right_head = mid.next
        mid.next = None  # Split the list

        # Step 2: Recursively sort both halves
        left_sorted = self.sortList(head)
        right_sorted = self.sortList(right_head)

        # Step 3: Merge sorted halves
        return self.merge(left_sorted, right_sorted)

    def getMiddle(self, head: ListNode) -> ListNode:
        """ Find the middle node using slow & fast pointers. """
        slow, fast = head, head
        prev = None  # To keep track of node before mid
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        return prev  # prev is the middle node

    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:
        """ Merge two sorted linked lists """
        dummy = ListNode()  # Dummy node to simplify merging
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        # Attach any remaining elements
        tail.next = l1 if l1 else l2

        return dummy.next  # Return merged sorted list

# Helper function to create a linked list from a list
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Debugging - Create and sort a linked list
values = [7, 5, 1, 9, 3, 2, 8, 4]  # Test case
head = create_linked_list(values)

print("Original Linked List:")
print_linked_list(head)

# Sorting the linked list
solution = Solution()
sorted_head = solution.sortList(head)

print("\nSorted Linked List:")
print_linked_list(sorted_head)
