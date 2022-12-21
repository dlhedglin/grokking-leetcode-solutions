# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        reversedList = self.reverseList(self.findMiddle(head))
        # tmp = head
        # while tmp:
        #     print(tmp.val)
        #     tmp = tmp.next
        # print('')
        # tmp = reversedList
        # while tmp:
        #     print(tmp.val)
        #     tmp = tmp.next

        while head and head.next and reversedList and reversedList.next:
            print(head.val)
            nextNode = head.next
            head.next = reversedList
            reversedList = reversedList.next
            head.next.next = nextNode
            head = head.next.next



    def findMiddle(self, head) -> ListNode:
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    def reverseList(self, head) -> ListNode:
        prevNode = None
        while head:
            nextNode = head.next
            head.next = prevNode
            prevNode = head
            head = nextNode
        return prevNode