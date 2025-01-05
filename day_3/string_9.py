"""
Problem:
Given a string s, find the first and last index of occurrence for each character present in the string. Return the results as a dictionary where the keys are characters, and the values are tuples representing the first and last index.

Example:

Input: "aabbcda"
Output: {'a': (0, 6), 'b': (2, 3), 'c': (4, 4), 'd': (5, 5)}

Input: "xyz"
Output: {'x': (0, 0), 'y': (1, 1), 'z': (2, 2)}

"""
# My Approach :
# def find_occurrance(s):
#     result = {s[0]:[0,0]}
#     for i in range(1,len(s)):
#         if s[i] in result.keys():
#             result[s[i]][1] = i
#         else:
#             result[s[i]] = [i,i]
    
#     return result

# Imporovements :-------
def find_occurrance(s):
    result = {}  # Start with an empty dictionary , handle edge case like for empty string 
    for i in range(len(s)):  # Start from the first character
        if s[i] in result:
            result[s[i]][1] = i  # Update the last index
        else:
            result[s[i]] = [i, i]  # Set both first and last index as same

    # Convert lists to tuples for immutability
    return {char: tuple(indexes) for char, indexes in result.items()}


print(find_occurrance(input("Enter value: ")))