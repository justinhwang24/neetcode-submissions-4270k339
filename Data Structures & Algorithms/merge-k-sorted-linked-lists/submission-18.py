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

        curr = lists.pop()
        while lists:
            a = lists.pop()
            curr = mergeLists(curr, a)
        return curr