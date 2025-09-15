class Stack:
    def __init__(self):
        self.items=[]

    def push(self,x):
        self.items.append(x)

    def is_empty(self):
        return len(self.items)==0

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        x=self.items.pop()
        return x

    def top(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.items[-1]

    def size(self):
        if self.is_empty():
            print("Stack is empty")
        return len(self.items)

    def display(self):
        if self.is_empty():
            print("Stack is empty")

        for i in range(len(self.items)-1,-1,-1):
            print(self.items[i],end=" ")
        print()

stack=Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.display()
print("top:",stack.top())
print("popped",stack.pop())

stack.push(4)
print("top:",stack.top())
stack.pop()
stack.pop()
stack.pop()
stack.display()