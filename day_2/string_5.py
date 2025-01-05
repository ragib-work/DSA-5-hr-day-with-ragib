"""
Problem Statement:
Write a function to remove leading, trailing, and extra spaces from a given string. Ensure that words in the string are separated by a single space.

Input:
A string s containing words separated by spaces, which may include leading, trailing, or multiple spaces between words.

Output:
A string with leading and trailing spaces removed, and all words separated by a single space.

Example 1:

 input : "  Hello   World  "
 output : "Hello World"


"""



"""
FIRST APPROACH USING INBUILT METHOD
"""
# Using Inbuilt Method:
# def remove_extra_spaces(s):
#     # Strip the leading/trailing spaces and split string into words
#     words = s.strip().split()
#     result = ' '.join(words)
#     return result



"""
SECOND APPROACH USING OWN CUSTOM LOGIC
"""

def remove_extra_spaces(s):
    result = ""
    in_space = False # it represents that just before this we have added a space to string (result) or not

    for i in range(len(s)):
        char = s[i]
        if char == ' ':
            if result!= '' and not in_space:
                result+=char
                in_space=True # because just before we have added space so now it's become True that track that we added just before it
        else:
            result += char
            in_space = False # because just before we have added letters , so it will become false , because it indicates that just before we added a space or Not

    # remove trailing space
    # because to check trailing space we need to access last index of string
    # so one edge cases we have to keep in mind before checking the last index
    # and that is result string must not be empty string , if it will be empty string and we go for last index it will throw error

    if result and result[-1] == ' ':
        result = result[:-1]

    return result


# take input from Users :
s = input("Enter the Value: ")
print(remove_extra_spaces(s))