def count_case_letters(c):
    upper_case = sum(1 for char in c if char.isupper())
    lower_case = sum(1 for char in c if char.islower())
    print(f"Upper case: {upper_case}")
    print(f"lower case: {lower_case}")
string =  input("Enter a string: ")
count_case_letters(string)