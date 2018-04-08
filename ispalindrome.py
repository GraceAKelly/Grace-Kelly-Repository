# Grace Kelly 10 March 2018

# Write a function ispalindrome that takes a string # 
# and returns True if the string is
# a palindrome and False otherwise

# https://github.com/ianmcloughlin/problems-python-fundamentals

def ispalindrome(s): # Define what you want to output
ans = True #Answer is true if
for i in range(len(s)): # Loop thro range 
if s[i] != s[len(s) - i - 1]: # if first character is not equal to last character 
ans = False # answer is false
return ans
# Tests from question.
print(ispalindrome("radar"))
print(ispalindrome("radars"))
