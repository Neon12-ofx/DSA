def palindrome_string(string,start,end):
    while start < end:
        if string[start]!=string[end]:
            return False
        start+=1
        end-=1
    return True

s=input("Enter String:")
print(palindrome_string(s,0,len(s)-1))