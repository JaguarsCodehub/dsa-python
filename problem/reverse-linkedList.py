class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_linked_list(head):
    prev = None
    current  = head

    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next

    return prev


# Helper function to create a linked list from a list
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print a linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Create, reverse, and print a linked list
head = create_linked_list([1, 2, 3, 4, 5])
print("Original:")
print_linked_list(head)

reversed_head = reverse_linked_list(head)
print("Reversed:")
print_linked_list(reversed_head)
