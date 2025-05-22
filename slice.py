# a python file for the strings portion for the module, parts 1 and 2

s = "Python is amazing!"        # declare a string 

print("first word: " + s[0:6])      # grab "Python"
print("amazing part " + s[10:len(s)])       # grab "amazing"
print("reversed string: " + s[::-1])        # reverse th string


s = " hello, python world! "            # create a new string

print(s.strip())                        # split the string by spaces
print(s.strip().capitalize())                   # capitalize the first
print(s.replace("world", "universe"))   # replace world with universe
print(s.upper())                        # convert to uppercase string


