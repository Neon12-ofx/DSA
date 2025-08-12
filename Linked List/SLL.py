class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class SLL:
    def __init__(self):
        self.head=None

    def append(self,val):
        new_node=Node(val)
        if self.head==None: # SLL is empty
            self.head=new_node
        else:
            curr=self.head
            while curr.next is not None:
                curr=curr.next
            curr.next=new_node

    def Tranversal(self):
        if self.head == None:
            print("Empty List")
        else:
            curr=self.head
            while curr is not None:
                print(curr.val,end=" ")
                curr=curr.next

    def insert(self,val,pos):
        new_node=Node(val)
        if pos==0:
            new_node.next=self.head
            self.head=new_node
        else:
            curr=self.head
            prev=None
            count=0
            while curr is not None and count<pos:
                prev=curr
                curr=curr.next
                count+=1
            prev.next=new_node
            new_node.next=curr

    def delete(self,val):
        curr=self.head
        if curr.val==val:
            self.head=curr.next
            return
        else:
            found=False
            prev=None
            while curr is not None:
                if curr.val==val:
                    found=True
                    break
                prev=curr
                curr=curr.next
                if found:
                    prev.next=curr.next
                    return
                else:
                    print("NO ELEMENT FOUND")
sll=SLL()
sll.append(1)
sll.append(2)
sll.append(3)
sll.insert(12,2)
sll.insert(15,5)
sll.delete(15)
sll.delete(1)
sll.Tranversal()