"""
Generate all possible substrings of a string.

"""

def all_substring(s):
    n = len(s)
    sub = []
    for i in range(n):
        result = s[i]
        sub.append(result)
        for j in range(i+1, n):
            result += s[j]
            sub.append(result)
    
    return sub

print(all_substring("Hello"))
