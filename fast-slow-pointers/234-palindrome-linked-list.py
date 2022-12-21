# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True
        ## find middle of linked list
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        slow = self.reverseList(slow)

        while head and slow:
            print(head.val, slow.val)
            print(head.next, slow.next)
            if head.val != slow.val:
                return False
            head = head.next
            slow = slow.next
        return True
    
    def reverseList(self, head) -> ListNode:
        prevNode = None
        while head:
            nextNode = head.next
            head.next = prevNode
            prevNode = head
            head = nextNode
        return prevNode