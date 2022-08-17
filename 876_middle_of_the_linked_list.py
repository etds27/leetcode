# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i = 0
        fast = head
        slow = head
        while fast is not None:
            if i % 2:
                slow = slow.next


            fast = fast.next
            i += 1

        return slow
