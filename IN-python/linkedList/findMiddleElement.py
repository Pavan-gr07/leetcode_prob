# 876. Middle of the Linked List
# Solved
# Easy
# Topics
# Companies
# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.

 

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.
# Example 2:


# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

# main.py

from linkedNode.node import ListNode

def findMiddleElement(head):
    """
    Finds the middle node in a linked list.
    Uses the fast and slow pointer approach.
    
    :param head: The head of the linked list
    :return: The middle ListNode
    """
    slow = fast = head
    
    # Move fast pointer twice as fast as slow pointer
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

def main():
    # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    
    # Link the nodes
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    # Call the findMiddleElement function with the head of the list
    middle = findMiddleElement(node1)
    
    # Print the middle node's value
    print("The middle node is:", middle)
    # For example, with a list of 5 nodes, this prints: ListNode(3)

if __name__ == "__main__":
    main()
