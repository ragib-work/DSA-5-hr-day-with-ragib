"""
Problem:
Given a string s, check if it contains two or three consecutive identical characters at any position. Return True if such a pattern exists, otherwise return False.

Example:

Input: "aabbccc"
Output: True

Input: "abcdef"
Output: False

Input: "aaab"
Output: True

"""

def check_consecutive(s):
    count = 1  # Start with 1 because a character itself counts as one occurrence
    prev = s[0]  # Set the first character as the previous character

    for char in s[1:]:  # Start loop from the second character
        if char == prev:
            count += 1
            if count >= 2:  # Found two or more consecutive identical characters
                return True
        else:
            prev = char
            count = 1  # Reset count to 1 for the new character

    return False


print(check_consecutive(input("Enter a value: ")))

        