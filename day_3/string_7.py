"""
Problem:
Given a string s, find the characters with the maximum and minimum frequency. Return the results as a tuple: (max_char, min_char). If multiple characters have the same frequency, return the lexicographically smallest one.

Example:

Input: "aabbccc"
Output: ('c', 'a')

Input: "xyz"
Output: ('x', 'x')


"""

def find_max_min_char(s):
    
    freq = [0]*26  # Initialize a dictionary-like structure for character frequency

    for char in s:
        index = ord(char)-ord('a')    # Calculate index for 'a' to 'z'
        freq[index]+=1
    
    max_count = 0
    min_count = float('inf')
    max_char = min_char = ''
    for i in range(26):   
        if freq[i]>0:    # Only consider characters present in the string
            if freq[i]>max_count:
                max_count = freq[i]
                max_char = chr(i+ord('a'))
            if freq[i]<min_count:
                min_count = freq[i]
                min_char = chr(i+ord('a'))
    
    return (max_char,min_char)

print(find_max_min_char(input("Enter String: ")))        



    
     