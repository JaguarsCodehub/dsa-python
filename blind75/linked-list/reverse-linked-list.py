def reverse(self):
        prev = None
        curr = self.head

        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        return prev