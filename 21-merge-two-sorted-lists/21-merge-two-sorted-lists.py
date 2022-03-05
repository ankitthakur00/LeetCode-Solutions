# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None or (l2 and l1.val>l2.val):
            l1, l2 = l2, l1
        tail = l1
        while tail and l2:
            if tail.next is None or (tail.next.val > l2.val):
                tail.next, l2 = l2, tail.next
            tail = tail.next
        return l1    
    # solution 2, same as OP's solution 1
    def mergeTwoLists1(self, l1, l2):
        head = tail = ListNode(0)
        while l1 and l2:
            if l1.val<=l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 if l1 else l2 # a better way is tail.next = l1 or l2, as in OP's code
        return head.next
