def is_palindrome(s):
    return s == s[::-1]
string =  input("Enter a string: ")
if is_palindrome(string):
    print("The string is a polinfrome")
else:
    print("The string is not a polindrome")


    