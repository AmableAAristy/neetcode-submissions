# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        brutus = []


        while list1:
            brutus.append(list1.val)
            list1 = list1.next

        while list2:
            brutus.append(list2.val)
            list2 = list2.next

        brutus.sort()
        dummy = ListNode()
        ans = dummy

        for i in brutus:
            dummy.next = ListNode(i)
            dummy = dummy.next
            


        return ans.next
            
