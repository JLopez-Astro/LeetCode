# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        listNode = []
        while head != None:
            listNode.append(head)
            head = head.next
        return listNode[len(listNode)//2]