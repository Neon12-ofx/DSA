def palindrome_no(Reserve_no,Original_no):
    if(Reserve_no==Original_no):
        print("Palindrome")
    else:
        print("Not Palindrome")


n=int(input("Enter the Number"))
num=n
result=0
while(num>0):
    last_digit=num%10
    result=(result*10)+last_digit
    num=num//10

print(f"the reverse no is:{result}")

palindrome_no(result,n)