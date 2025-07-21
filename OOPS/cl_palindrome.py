class palindrome:
    def __init__(self,string,start,end):
        self.string=string
        self.start=start
        self.end=end

    def palin_check(self):
        while self.start<self.end:
            if self.string[self.start]!=self.string[self.end]:
                return False
            self.start+=1
            self.end-=1
        return True

s=input("Enter String:")
a=palindrome(s,0,len(s)-1)
print("Palindrome",a.palin_check())