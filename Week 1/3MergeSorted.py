# Approach: We can have two pointers, each at the start of both the lists.
# compare elements on both pointer and place on third list accordingly
# Time O(n+m) | space O(n+m)
# If we use linked list we can insert in one of the list instead of creating another list
# Time O(n+m) | space O(1)

# Approach 2: Treat both the list as stack, keep popping and pushing after comparision
def mergeTwoLists(list1, list2):
    final_list = []
    while len(list1) > 0 and len(list2) > 0:
        if list1[0] < list2[0]:
            final_list.append(list1.pop(0))
        else:
            final_list.append(list2.pop(0))
    final_list += list1 if len(list1) > 0 else list2
    return final_list

list1 = [1, 12, 15, 16]
list2 = [1, 10, 11, 17]
print(mergeTwoLists(list1, list2))


"""
Leetcode using linked list:
https://leetcode.com/problems/merge-two-sorted-lists/submissions/
Time O(min(n, m)) | space O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_list = ListNode()
        result = new_list
        
        ptr1 = list1
        ptr2 = list2
        
        while ptr1 is not None and ptr2 is not None:
            # print(f"ptr1 {ptr1.val}, ptr2 {ptr2.val}")
            if ptr1.val < ptr2.val:
                new_list.next = ptr1
                ptr1 = ptr1.next
            else:
                new_list.next = ptr2
                ptr2 = ptr2.next
            new_list = new_list.next
            
        if ptr1 is not None:
            new_list.next = ptr1
        if ptr2 is not None:
            new_list.next = ptr2
            
        result = result.next
        return result
"""