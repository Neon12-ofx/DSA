def palindrome_string(s,l,r):
    if(l>=r):
        return True
    if s[l]!=s[r]:
        return False
    return palindrome_string(s,l+1,r-1)

string=input("enter a string")
print(palindrome_string(string,0,len(string)-1))