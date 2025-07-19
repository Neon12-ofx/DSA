#Head Recursion means that the job is first done and then func is called
count=0
def func(name):
    global count
    if count==4:
        return
    print(F"{name}")
    count+=1
    func(name) #<---------------the function is recursively called at last

#Tail Recursion means that the function is first called then the job is done afterward
def func2(namae):
    global count
    if count==4:
        return
    count+=1
    func2(namae)
    print(F"{namae}")



n=input("Name:")
func(n)
func2(n)