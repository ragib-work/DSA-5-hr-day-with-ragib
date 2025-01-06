"""
### **Problem Statement:**  
**Reverse a Given Number**  
Given a positive integer `n`, write a program to **reverse its digits**. The reversed number should not have any leading zeroes.

---

**Input:**  
- An integer `n` (where `n ≥ 0`).

**Output:**  
- An integer representing the reversed number.

---

**Example 1:**  
```text
Input:  
n = 12345  

Output:  
54321
```

**Example 2:**  
```text
Input:  
n = 1000  

Output:  
1
```

---

**Explanation:**  
- In **Example 1**, reversing `12345` gives `54321`.  
- In **Example 2**, reversing `1000` removes the leading zeroes, resulting in `1`.

"""



def reverse_number(n):
    rev_num = 0
    while n > 0:
        last_digit = n%10
        rev_num = rev_num*10 + last_digit
        n //= 10
    return rev_num


n = 1000
print(reverse_number(n))