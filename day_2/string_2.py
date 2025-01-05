"""
Problem Statement:
Write a function to count the number of letters, digits, and special characters in a given string.

Input:
A string s of length

Output:
Print three integers:

The count of letters (both uppercase and lowercase).
The count of digits.
The count of special characters (any character that is not a letter or digit).

Example :
input: Hello123!

output : 5 3 1

"""
from string import digits


def count_chars(s):
    letters = 0
    digits = 0
    s_chars = 0
    for i in s:
        i = ord(i)
        if ord("a") <= i <=ord("z") or ord("A")<= i <=ord("Z"):
           letters+=1
        elif ord("0")<= i <=ord("9"):
            digits+=1
        else:
            s_chars+=1
    return [letters,digits,s_chars]

s = input("Enter a String: ")
print(*count_chars(s))