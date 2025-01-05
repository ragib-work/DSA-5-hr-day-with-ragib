"""
Problem:
Given a string s, check if it contains all the letters from 'a' to 'z' at least once. Return True if it does, otherwise return False.

Example:

Input: "abcdefghijklmnopqrstuvwxyz"
Output: True

Input: "The quick brown fox jumps over the lazy dog"
Output: True

Input: "hello world"
Output: False

"""
# My appraoch :------------------------
# def contains_a_to_z(s):
#     s = s.lower()
#     letters = [s[0]]
#     for char in s[1:]:
#         if char!= ' ' and char not in letters:
#             letters.append(char)

#     if len(letters)== 26:
#         return True
#     else:
#         return False


# What Can Be Improved:
# Inefficient membership check:

# Using char not in letters in a list has a time complexity of O(n) for each check. This makes your solution less efficient, especially for long strings.
# Instead, using a set is more efficient because membership checks in sets are O(1).
# Handling spaces:

# Your solution checks char != ' ' to skip spaces. Instead, you can simplify by directly checking if the character is a letter ('a' <= char <= 'z').
# Simplify condition:

# The if len(letters) == 26 check can be directly returned as a boolean without needing the if-else block.


# Improved Solution:--------------------------
def contains_a_to_z(s):
    s = s.lower()
    letters = set()  # Use a set instead of a list

    for char in s:
        if 'a' <= char <= 'z':  # Only add alphabetic characters
            letters.add(char)
        if len(letters) == 26:  # Early exit
            return True

    return False


print(contains_a_to_z(input("Enter Value: ")))
        


