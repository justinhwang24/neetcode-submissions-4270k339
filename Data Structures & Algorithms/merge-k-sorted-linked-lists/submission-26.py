# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(listA, listB):
            head = ListNode()
            curr = head
            while listA and listB:
                if listA.val <= listB.val:
                    curr.next = listA
                    listA = listA.next
                else:
                    curr.next = listB
                    listB = listB.next
                curr = curr.next
            curr.next = listA or listB
            return head.next
        
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i+1 < len(lists) else None
                merged.append(merge(l1, l2))
            lists = merged
        return lists[0]