# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = None  # Initialize head pointer for the result list
        tail = None  # Initialize tail pointer for the result list
        carry = 0    # Carry to hold the overflow value during addition

        # Loop continues until both lists are empty and no carry remains
        while l1 or l2 or carry:
            # Step 1: Initialize sumVal with carry value
            sumVal = carry

            # Step 2: Add l1's value if available
            if l1:
                print(f"Adding l1.val: {l1.val}")
                sumVal += l1.val
                l1 = l1.next  # Move l1 pointer to next node

            # Step 3: Add l2's value if available
            if l2:
                print(f"Adding l2.val: {l2.val}")
                sumVal += l2.val
                l2 = l2.next  # Move l2 pointer to next node

            # Step 4: Calculate new carry and digit value
            carry = sumVal // 10  # Extract carry for next iteration
            digit = sumVal % 10   # Extract the current digit
            print(f"Result digit: {digit}, New carry: {carry}")

            # Step 5: Create a new node for the digit
            temp = ListNode(digit)

            # Step 6: Append the node to the result list
            if not head:
                # First node becomes both head and tail
                head = temp
                tail = temp
            else:
                # Append the new node and move the tail forward
                tail.next = temp
                tail = temp

        # Step 7: Return the resulting linked list
        return head

# Utility function to create a linked list from a list of values
def createLinkedList(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Utility function to print the linked list
def printLinkedList(head):
    result = []
    while head:
        result.append(str(head.val))
        head = head.next
    print(" -> ".join(result))

# Sample Input
l1 = createLinkedList([2, 4, 3])   # Represents 342
l2 = createLinkedList([5, 6, 4])   # Represents 465

# Solution Execution
solution = Solution()
result = solution.addTwoNumbers(l1, l2)

# Output the result
print("Result Linked List:")
printLinkedList(result)
