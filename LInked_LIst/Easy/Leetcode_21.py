# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1,list2):
        head = ListNode(0)
        root = head

        while list1 and list2:
            if list1.val <= list2.val:
                head.next = list1
                head = list1
                list1 = list1.next
            else:
                head.next = list2
                head = list2
                list2 = list2.next
        head.next = list1 if list1 else list2
        return root.next