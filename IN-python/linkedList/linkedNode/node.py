# linkedList/node.py

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # Stores the node's value
        self.next = next  # Pointer to the next node

    def __repr__(self):
        return f"ListNode({self.val})"
