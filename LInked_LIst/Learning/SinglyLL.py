class SinglyLL:
    def __init__(self, value, next=None):
        self.value = value 
        self.next = next 
    
    def __str__(self):
        return str(self.value)

Node1 = SinglyLL("First Value")
Node2 = SinglyLL("Second Value")
Node3 = SinglyLL("Third Value")
Node4 = SinglyLL("Fourth Value")

Node1.next = Node2
Node2.next = Node3
Node3.next = Node4

# print(Node1)

## Traversing a List
curr = Node1
while curr:
    # print(curr)
    curr = curr.next

## Displaying Linked List
def display(Node):
    curr = Node
    elements = []
    while curr:
        elements.append(str(curr.value))
        curr = curr.next 
    print(' -> '.join(elements), '-> None')
# display(Node1)

## Search From Node Value
def search(head, val):
    curr = head
    while curr:
        if head.value == val:
            return True
        curr = curr.next 
    return False
# print(search(Node1, "FIrst Value"))

# print(Node1.next.next)

Node1.next = Node1.next.next
display(Node1)