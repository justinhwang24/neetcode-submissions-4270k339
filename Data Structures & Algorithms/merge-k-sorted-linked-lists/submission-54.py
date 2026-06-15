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
        
        if not lists or len(lists) == 0:
            return None
        while len(lists) > 1:
            newLists = []
            for i in range(0, len(lists), 2):
                listA = lists[i]
                listB = lists[i+1] if i+1 < len(lists) else None
                newLists.append(mergeLists(listA, listB))
            lists = newLists
        return lists[0]