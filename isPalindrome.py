# determine if a string is a palindrome for part 3

s = input("give me a string:")

low = 0
high = len(s) - 1
isPal = True
while low <= high:
    if s[low] != s[high]:                       # if not a palindrome
        isPal = False
        break
    else:
        low += 1
        high -= 1

if isPal:
    print("yes! " + s + " is a palindrome!")        # good case
else:
    print(s + " is not a palindrome")  