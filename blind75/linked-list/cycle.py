def hasCycle(self, head):
        slow, fast = head, head

        while fast & fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
