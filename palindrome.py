num  = int(input("Enter a number: "))
rev = 0
temp = num
while temp > 0:
    rem = temp%10
    rev = rem + (rev*10)
    temp = int(temp/10)
if num == rev:
    print("\n It is a Palindrome Number")
else:
    print("\n It is not a Palindrome Number")