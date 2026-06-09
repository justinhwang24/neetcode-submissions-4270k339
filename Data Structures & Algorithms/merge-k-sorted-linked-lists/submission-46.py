# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeLists(listA, listB):
            dummy = ListNode()
            cur = dummy
            while listA and listB:
                if listA.val < listB.val:
                    cur.next = listA
                    listA = listA.next
                else:
                    cur.next = listB
                    listB = listB.next
                cur = cur.next
            cur.next = listA or listB
            return dummy.next
        
        if not lists:
            return None
        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                merged.append(mergeLists(lists[i], lists[i+1] if i+1 < len(lists) else None))
            lists = merged
        return lists[0]