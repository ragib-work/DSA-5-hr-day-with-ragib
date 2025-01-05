"""

### **Problem Statement:**  
**Find a specific substring within a string.**  
Given a string `s` and a target substring `sub`, determine if the substring exists within the string. If it exists, return the starting index of its first occurrence. If it does not exist, return `-1`.

**Input:**  
- `s` (string): The main string.  
- `sub` (string): The target substring to find.  

**Output:**  
- An integer representing the starting index of the first occurrence of `sub` in `s`, or `-1` if the substring is not found.

**Example:**  
```text
Input: s = "hello world", sub = "world"  
Output: 6  

Input: s = "datastructures", sub = "struct"  
Output: 4  

Input: s = "abcdef", sub = "xyz"  
Output: -1
```

"""

def check_substring(s,sub):
    n = len(s)
    for i in range(n):
        