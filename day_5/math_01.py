"""


### **Problem Statement:**  
**Find the Sum of Digits of a Number**  
Given a positive integer `n`, write a program to calculate the **sum of its digits**. The solution should handle large numbers efficiently.

---

**Input:**  
- An integer `n` (where `n ≥ 0`).

**Output:**  
- An integer representing the sum of the digits of `n`.

---

**Example 1:**  
```text
Input:  
n = 12345  

Output:  
15
```

**Example 2:**  
```text
Input:  
n = 9876  

Output:  
30
```

---

**Explanation:**  
- In **Example 1**, the sum of the digits of `12345` is `1 + 2 + 3 + 4 + 5 = 15`.  
- In **Example 2**, the sum of the digits of `9876` is `9 + 8 + 7 + 6 = 30`.

"""


def sum_of_digits(n):
    total_sum = 0
    while n > 0:
        digit = n % 10  # Get the last digit
        total_sum += digit  # Add it to the sum
        n //= 10  # Remove the last digit
    return total_sum
 





n = 9876  
print(sum_of_digits(n))