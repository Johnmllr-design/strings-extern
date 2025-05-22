# determine if a string is a palindrome for part 3

s = input("give me a string:")

low = 0                             # low pointer
high = len(s) - 1                   # high pointer
isPal = True                        # initially the palindrome is true
while low <= high:
    if s[low] != s[high]:                       # if not a palindrome
        isPal = False
        break
    else:
        low += 1                    # check next pointer
        high -= 1                   # check next pointer

if isPal:
    print("yes! " + s + " is a palindrome!")        # good case
else:
    print(s + " is not a palindrome")  
