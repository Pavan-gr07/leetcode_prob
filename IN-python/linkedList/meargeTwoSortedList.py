# 205. Merge Two Sorted Lists
# LinkedList
# Salesforce
# Cisco
# Adobe



# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.



# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Input: list1 = [1], list2 = [0]
# Output: [0,1]

# Constraints:
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoSortedListsIterative(l1, l2):
    dummy = ListNode()  # Dummy node as a starting point
    tail = dummy

    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    # Attach the remaining nodes
    tail.next = l1 if l1 else l2

    return dummy.next  # Return the merged list without dummy node

def printList(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

l1 = ListNode(1, ListNode(3, ListNode(5)))
l2 = ListNode(2, ListNode(4, ListNode(6)))


# Example usage remains the same
merged = mergeTwoSortedListsIterative(l1, l2)
printList(merged)





