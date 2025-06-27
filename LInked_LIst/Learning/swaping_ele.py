class SinglyLL:
    def __init__(self, value, next=None):
        self.value = value 
        self.next = next 
    
    def __str__(self):
        return str(self.value)

Node1 = SinglyLL(2)
Node2 = SinglyLL(2)
Node3 = SinglyLL(0)
Node4 = SinglyLL(1)

Node1.next = Node2
Node2.next = Node3
Node3.next = Node4

curr = Node1
while curr:
    print(curr.value, "->", end="")
    curr = curr.next

ptr1 = Node1
while ptr1:
    ptr2 = ptr1.next
    while ptr2:
        if ptr2.value < ptr1.value:
            temp = ptr1.value
            ptr1.value = ptr2.value
            ptr2.value = temp
            
        ptr2 = ptr2.next
    ptr1 = ptr1.next 

curr = Node1
while curr:
    print(curr.value, "->", end="")
    curr = curr.next