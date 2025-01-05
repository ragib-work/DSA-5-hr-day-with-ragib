"""
Remove the first, last, and Kth character from a string.

"""


def remove_char(s,k):
    n = len(s)
    result = ''
    for i in range(1,n-1):
        if i!= k-1 :
            result+=s[i]
    return result

print(remove_char("xHello x World!x",8))