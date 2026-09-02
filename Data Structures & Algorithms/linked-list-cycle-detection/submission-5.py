# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        f, s = head, head
        while True:
            if f == None or s.next == None:
                return False
            f = f.next.next if f.next != None else None
            s = s.next
            if f == s:
                return True
            
            