class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class Sll:
    def __init__(self):
        self.head=None
    def inserten(self,val):
        new_node=Node(val)
        if self.head==None:
            self.head=new_node
        else:
            curr=self.head
            while curr.next!=None:
                curr=curr.next
            curr.next=new_node

    def Traverse(self):
        if self.head==None:
            print("No node")
        else:
            curr=self.head
            while curr is not None:
                print(curr.val, end=" ")
                curr=curr.next

    def insertatany(self,val,pos):
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

    def deleteat(self,val):
        curr=self.head
        if curr.val==val:
            self.head=curr.next
            return
        else:
            prev=None
            while curr is not None:
                if curr.val==val:
                    prev.next = curr.next
                    return
                prev=curr
                curr=curr.next
        print("No Element Found")


sll = Sll()

while True:
    print("\n=== Singly Linked List Menu ===")
    print("1. Insert at End")
    print("2. Insert at Any Position")
    print("3. Delete")
    print("4. Traverse")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        val = int(input("Enter value: "))
        sll.inserten(val)
    elif choice == "2":
        val = int(input("Enter value: "))
        pos = int(input("Enter position (0-based): "))
        sll.insertatany(val, pos)
    elif choice == "3":
        val = int(input("Enter value to delete: "))
        sll.deleteat(val)
    elif choice == "4":
        sll.Traverse()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.")