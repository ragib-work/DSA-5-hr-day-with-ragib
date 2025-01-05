"""
Problem Statement:
Task: Write a function to count the number of words in a given string. A word is defined as a sequence of non-space characters, and words are separated by spaces.

Input:
A string s containing words separated by spaces.

Output:
An integer representing the number of words in the string.

Constraints:
The input string may contain leading and trailing spaces.
Multiple spaces between words should be treated as a single space.
If the string is empty or contains only spaces, return 0.

Example 1:
Input : s = "   This is a   test  "
Output : 4

Example 2:
Input : s = ' '
Output : 0

"""

def count_words(s):
    count = 0
    in_words = False   # Flag that indicate that we are in words or Not
    for char in s:
        if char!= ' ':
            if not in_words:
                count+=1
                in_words = True
        else:
            in_words = False

    return count

s = input("Enter the Value: ")
print(count_words(s))
