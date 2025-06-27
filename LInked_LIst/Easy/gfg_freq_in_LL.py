"""  
class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
  This is method only submission.
  You only need to complete the method.
"""
class Solution:
    def count(self, head, key):
        # Code here
        freq = 0
        curr = head
        
        while curr:
            if curr.data == key:
                freq += 1
            curr = curr.next
        return freq