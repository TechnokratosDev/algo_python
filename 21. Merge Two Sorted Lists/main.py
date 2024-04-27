# 1, 2, 4
# 1, 3, 4, 5
# 1, 1, 2, 3, 4, 4
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[
        ListNode]:
        result = None
        curr = None

        curr1 = list1
        curr2 = list2

        while curr1 is not None and curr2 is not None:
            if curr1.val < curr2.val:
                if result is None:
                    result = ListNode(val=curr1.val)
                    curr = result
                else:
                    curr.next = ListNode(val=curr1.val)
                    curr = curr.next
                curr1 = curr1.next
            else:
                if result is None:
                    result = ListNode(val=curr2.val)
                    curr = result
                else:
                    curr.next = ListNode(val=curr2.val)
                    curr = curr.next
                curr2 = curr2.next

        while curr1 is not None:
            if result is None:
                result = ListNode(val=curr1.val)
                curr = result
            else:
                curr.next = ListNode(val=curr1.val)
                curr = curr.next
            curr1 = curr1.next

        while curr2 is not None:
            if result is None:
                result = ListNode(val=curr2.val)
                curr = result
            else:
                curr.next = ListNode(val=curr2.val)
                curr = curr.next
            curr2 = curr2.next

        return result
