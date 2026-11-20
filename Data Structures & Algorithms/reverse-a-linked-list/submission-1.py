# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        # print(cur.val)
        prev = None
        while cur:
            next_node = cur.next
            prev = ListNode(cur.val, prev)  
            cur = next_node          
        return prev

        