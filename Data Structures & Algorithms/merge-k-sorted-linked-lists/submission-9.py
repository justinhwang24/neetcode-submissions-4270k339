# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return
        dummy = None
        for node in lists:
            dummy = self.merge(dummy, node)
        return dummy

    def merge(self, left, right) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        l = left
        r = right

        while l and r:
            if l.val <= r.val:
                curr.next = l
                l = l.next
            else:
                curr.next = r
                r = r.next
            curr = curr.next
        while l:
            curr.next = l
            l = l.next
            curr = curr.next
        while r:
            curr.next = r
            r = r.next
            curr = curr.next
        return dummy.next
