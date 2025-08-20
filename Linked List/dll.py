class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None

    def insert_at_head(self,val):
        new_node=Node(val)
        new_node.next=self.head
        if self.head is not None:
            self.head.prev=new_node
        self.head=new_node

    def insert_at_tail(self,val):
        new_node=Node(val)
        if self.head is None:
            self.head=new_node
        else:
            curr=self.head
            while curr.next is not None:
                curr=curr.next
            curr.next=new_node
            new_node.prev=curr

    def insert_at_index(self,val,index):
        new_node=Node(val)
        if index==0:
            self.insert_at_head(new_node)
        else:
            curr=self.head
            count=0
            while curr is not None and count < index-1:
                curr=curr.next
                count+=1
            if count == None:
                print("Index out of range")

            new_node.next=curr.next
            new_node.prev=curr
            if curr.next is not None:
                curr.next.prev=new_node
            curr.next=new_node

    def traverse(self):
        curr=self.head
        while curr is not None:
            print(curr.val,end=" ")
            curr=curr.next
    def delete_at_first(self):
        curr= self.head
        self.head=self.head.next
        if self.head is not None:
            self.head.prev=None
        curr.next = None

    def delete_at_last(self):
        curr=self.head
        while curr.next is not None:
            curr=curr.next
        curr.prev.next=None
        curr.prev=None

    def delete_at_index(self,index):
        if index==0:
            self.delete_at_first()
            return
        else:
            curr=self.head
            count=0
            while curr is not None:
                if count == index:
                    if curr.next is not None:
                        curr.next.prev = curr.prev
                    if curr.prev is not None:
                        curr.prev.next=curr.next
                    curr.prev=None
                    curr.next=None
                    print(f"Deleting index {index}, value = {curr.val}")
                    return
                curr=curr.next
                count+=1


dll=DoublyLinkedList()
dll.insert_at_head(1)
dll.insert_at_head(2)
dll.insert_at_tail(3)
dll.insert_at_tail(4)
dll.insert_at_index(5,2)
dll.delete_at_first()
dll.delete_at_last()
dll.delete_at_index(1)
dll.traverse()