class Solution:
    def sort(self,n):
        self.n=n
        s=len(self.n)
        for i in range(s-2,-1,-1):
            is_swap=False
            for j in range(0,i+1):
                if(self.n[j]>self.n[j+1]):
                    self.n[j],self.n[j+1]=self.n[j+1],self.n[j]
                    is_swap=True
            if(is_swap==False):
                break
        return self.n

arr=list(map(int,input().split()))
obj=Solution()
print(obj.sort(arr))