class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

### Task start here

    def insert(self, head, data):
        if not head:
            head = Node(data)
        elif not head.next:
            head.next = Node(data)
        else:
            self.insert(head.next, data)
        return head


### Task end here


mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
mylist.display(head);