class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        rs = ListNode(0)
        current = rs
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        if list1 is not None:
            current.next = list1
        else:
            current.next = list2
        rs = rs.next
        return self.merge_sort(rs)
    
    def merge_sort(self, head):
        if head is None or head.next is None:
            return head
        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        left = self.merge_sort(head)
        right = self.merge_sort(mid)
        return self.merge(left, right)
    
    def merge(self, l1, l2):
        rs = ListNode(0)
        current = rs
        
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        
        if l1 is not None:
            current.next = l1
        else:
            current.next = l2
        
        return rs.next