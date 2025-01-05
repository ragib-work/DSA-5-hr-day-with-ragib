"""
Write a function to find the difference between the number of consonants and vowels in a given string.

Input:
A string s containing alphabetic characters, spaces, and special characters.

Output:
An integer representing the difference between the number of consonants and vowels (i.e.,
Consonants−Vowels).

Examples:

    input : Programming@Python

    output :

"""

def diff_cons_vowel(s):
    vowels = 0
    consonants = 0
    for i in s:
        if "a" <= i <= "z" or "A" <= i <= "Z":
            if i in "aeiouAEIOU":
                vowels+=1
            else :
                consonants+=1
    return consonants-vowels

s = input("Enter a String: ")
print(diff_cons_vowel(s))
