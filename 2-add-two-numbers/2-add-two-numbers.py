# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        res=ListNode(0)
        temp=res
        rem=0
        while l1 and l2:
            s=l1.val+l2.val+rem
            if s>=10:
                rem=1
            else:
                rem=0
            temp.next=ListNode(s%10)
            temp=temp.next
            l1=l1.next
            l2=l2.next
            
        while l1:
            s=l1.val+rem
            if s>=10:
                rem=1
            else:
                rem=0
            temp.next=ListNode(s%10)
            temp=temp.next
            l1=l1.next
        
        while l2:
            s=l2.val+rem
            if s>=10:
                rem=1
            else:
                rem=0
            temp.next=ListNode(s%10)
            temp=temp.next
            l2=l2.next
        
        if rem:
            temp.next=ListNode(rem)
            
            
        return res.next
        