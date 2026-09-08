# Definition for singly-linked list.
from typing import Optional

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev


if __name__ == "__main__":
    # Example: [1, 2, 3, 4, 5]
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    solution = Solution()
    result = solution.reverseList(head)

    # Print result: [5, 4, 3, 2, 1]
    while result:
        print(result.val, end=" ")
        result = result.next
