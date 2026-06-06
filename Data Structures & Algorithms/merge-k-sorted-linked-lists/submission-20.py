# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeLists(nodeA, nodeB):
            dummy = ListNode()
            curr = dummy
            while nodeA and nodeB:
                if nodeA.val <= nodeB.val:
                    curr.next = nodeA
                    nodeA = nodeA.next
                else:
                    curr.next = nodeB
                    nodeB = nodeB.next
                curr = curr.next
            curr.next = nodeA or nodeB
            return dummy.next
        
        if not lists:
            return None

        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merged.append(mergeLists(l1, l2))
            lists = merged
        return lists[0]