class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carryOver = 0
        result = ListNode(-1)
        resultTail = result
        
        while l1 or l2:
            total = 0
            if l1: 
                total += l1.val
                l1 = l1.next
            if l2: 
                total += l2.val
                l2 = l2.next
            
            total += carryOver
            carryOver, remainder = divmod(total, 10)
            resultTail.next = ListNode(remainder)
            resultTail = resultTail.next
            
        if carryOver > 0:
            resultTail.next = ListNode(carryOver)
            
        return result.next