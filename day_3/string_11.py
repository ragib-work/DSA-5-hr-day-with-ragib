"""
Problem:
Write a function that takes a string s, a character c, and an integer k. The function should insert the character c at the first position, last position, and the Kth position in the string. Return the resulting string.

Example:

Input: s = "world", c = '!', k = 3
Output: "!wo!rld!"

Input: s = "abc", c = '#', k = 2
Output: "#a#bc#"

"""

# def insert_char(s:str, c:str, k:int)-> str :
#     li = list(s)
#     li.insert(k-1,c)
#     li.insert(0,c)
#     li.append(c)
#     result = ''.join(li)
#     return result

# 2. Optimized Approach:
def insert_char(s, c, k):
    result = c + s  # Insert character at the first position
    result = result[:k] + c + result[k:]  # Insert character at the Kth position (after adding the first character)
    result += c  # Insert character at the last position
    return result


# 3. without INBUILT-METHOD :
def insert_char(s: str, c: str, k: int) -> str:
    n = len(s)
    result = ""

    # Insert the character at the first position
    result += c

    # Insert characters from the original string
    for i in range(n):
        # Insert the character at the Kth position
        if i == k - 1:
            result += c
        result += s[i]

    # Insert the character at the last position
    result += c

    return result


print(insert_char("world", '!',3))
    
