# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:


        carry = 0
        output = None


        while True:
            # If both lists are finished break the loop
            if l1 is None and l2 is None:
                if carry:
                    temp = output
                    output = ListNode(carry, None)
                    temp.next = output
                break

            # If a singular list is finished, pad zeros
            if l1 is None:
                l1_val = 0
            else:
                l1_val = l1.val
                l1 = l1.next

            if l2 is None:
                l2_val = 0
            else:
                l2_val = l2.val
                l2 = l2.next

            new_val = l1_val + l2_val + carry

            # Adjust for the carry by setting the carry value to 1 and subtracting 10
            if new_val > 9:
                carry = 1
                new_val -= 10
            else:
                carry = 0

            # print(l1_val, l2_val, new_val, carry)


            temp = output
            output = ListNode(new_val, None)

            # print(temp)
            if temp is not None:
                temp.next = output
            else:
                starting_node = output


        return starting_node
