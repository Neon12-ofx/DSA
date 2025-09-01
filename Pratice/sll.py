class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class Sll:
    def __init__(self):
        self.head=None

    def append(self,val):
        new_node=Node(val)
        if self.head is None:
            self.head=new_node
        else:
            curr=self.head
            while curr is not None:
                curr=curr.next
            curr.next=new_node

    def insert_at_pos(self, val, pos):
        new_node=Node(val)
        if pos==0:
            new_node.next=self.head
            self.head=new_node
        else:
            curr=self.head
            prev=None
            count=0
            while curr is not None and count < pos:
                prev=curr
                curr=curr.next
                count+=1
            prev.next=new_node
            new_node.next=prev

    def traverse(self):
        curr=self.head
        if self.head is None:
            return
        else:
            while curr is not None:
                print(curr.val)
                curr=curr.next

    def remove_at_pos(self,pos):
        if self.head is None:
            return
        if pos==0:
            curr=self.head
            self.head=self.head.next
            curr.next=None
        else:

            curr=self.head
            prev=None
            count=0
            while curr is not None and count < pos:
                prev=curr
                curr=curr.next
                count+=1
            if curr is None:
                return
            prev.next=curr.next
            curr.next=None

    def middle_node(self):
        if self.head is None:
            return
        slow=self.head
        fast=self.head
        while fast is not None and fast.next is not None:
            fast=fast.next.next
            slow=slow.next
        return slow