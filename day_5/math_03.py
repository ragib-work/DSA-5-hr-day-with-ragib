"""
### **Problem Statement:**  
**Check if a Number is a Palindrome**  
Given a positive integer `n`, write a program to check whether the number is a **palindrome** or not. A number is considered a palindrome if it reads the same backward as forward.

---

**Input:**  
- An integer `n` (where `n ≥ 0`).

**Output:**  
- Return `True` if the number is a palindrome.  
- Return `False` otherwise.

---

**Example 1:**  
```text
Input:  
n = 121  

Output:  
True
```

**Example 2:**  
```text
Input:  
n = 123  

Output:  
False
```

---

**Explanation:**  
- In **Example 1**, the number `121` reads the same backward as forward, so it's a palindrome.  
- In **Example 2**, the number `123` does not read the same backward as forward, so it's not a palindrome.

"""


def reverse_num(n):
    rev_num = 0
    while n > 0:
        last_digit = n % 10
        rev_num = rev_num*10 + last_digit
        n //= 10
    return rev_num

def is_palindrome(n):
    if n == reverse_num(n):
        return True
    return False


n = 123
print(is_palindrome(n))