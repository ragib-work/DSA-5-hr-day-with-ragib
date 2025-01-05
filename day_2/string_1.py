"""
Problem Statement:
Write a function to print the ASCII value of each character in a given string.

Input:
A string s containing only printable characters.

Output:
For each character in s, print its ASCII value on a new line.

Sample Input:
Hello

Sample Output:
72
101
108
108
111

"""

def print_ascii(s):
    for i in s:
        print(ord(i))

s = input("Please Enter Word: ")
print_ascii(s)