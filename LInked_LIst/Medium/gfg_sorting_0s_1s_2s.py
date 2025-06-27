class Solution:
    def segregate(self, head):
        #code here
        # ptr1 = head
        # while ptr1:
        #     ptr2 = ptr1.next
        #     while ptr2:
        #         if ptr2.data < ptr1.data:
        #             temp = ptr1.data
        #             ptr1.data = ptr2.data
        #             ptr2.data = temp
            
        #         ptr2 = ptr2.next
        #     ptr1 = ptr1.next 
        # return head
        if head == None or head.next == None:
            return head
        
        curr = head
        l = [0,0,0]
        while curr:
            l[curr.data] += 1
            curr = curr.next
        
        curr = head
        ptr = 0
        while curr:
            ptr += 1
            if ptr <= l[0]:
                curr.data = 0
            elif ptr <= l[0]+l[1]:
                curr.data = 1
            else:
                curr.data = 2
            curr = curr.next
        return head