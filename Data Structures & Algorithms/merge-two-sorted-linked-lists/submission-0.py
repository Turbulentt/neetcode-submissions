# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2

        dummy = ListNode()
        newCurr = dummy

        while head1 and head2:
            if head1.val <= head2.val:
                newCurr.next = ListNode(head1.val)
                head1 = head1.next
            else:
                newCurr.next = ListNode(head2.val)
                head2 = head2.next
            newCurr = newCurr.next
        
        while head1:
            newCurr.next = ListNode(head1.val)
            newCurr = newCurr.next
            head1 = head1.next
        
        while head2:
            newCurr.next = ListNode(head2.val)
            newCurr = newCurr.next
            head2 = head2.next
        
        return dummy.next
