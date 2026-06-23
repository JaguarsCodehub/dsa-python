class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
    def traverse(self):
        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def length(self):
        temp = self.head
        count = 0

        while temp:
            count += 1
            temp = temp.next
            
        return count
    
    def search(self, key):
        temp = self.head

        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False
    
    def reverse(self):
        prev = None
        curr = self.head

        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        return prev
    
    def hasCycle(self, head):
        slow, fast = head, head

        while fast & fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


ll = LinkedList()
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.insert_at_end(40)

ll.traverse()
print(ll.length())
print(ll.search(50))