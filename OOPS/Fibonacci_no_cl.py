class Fibonacci:
    def fibo(self,n):
        self.n=n
        if(self.n==0 or self.n==1):
            return n
        return self.fibo(n-1)+self.fibo(n-2)
s=int(input())
obj=Fibonacci()
print(obj.fibo(s))