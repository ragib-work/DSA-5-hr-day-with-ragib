"""
Write a function to convert all uppercase letters in a given string to lowercase and all lowercase letters to uppercase. Non-alphabetic characters should remain unchanged.

Input:
A string s containing alphabetic characters, digits, spaces, and special characters.

Output:
A string with uppercase letters converted to lowercase and lowercase letters converted to uppercase.

Example 1:

input: Hello123

output: hELLO123


"""

def swap_cases(s):
    result = ""
    for i in s:
        if "a"<=i<="z":
           # this condition check the letter is lowercase
            result+=chr(ord(i)-32)
        elif "A"<=i<="Z":
            result+=chr(ord(i)+32)
        else:
            result+=i
    return result

s = input("Enter the Value: ")
print(swap_cases(s))
