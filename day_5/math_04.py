"""
### **Problem Statement:**  
**Check if a Number is an Armstrong Number**  
Given a positive integer `n`, write a program to determine if the number is an **Armstrong number**. An Armstrong number (also known as a **narcissistic number**) is a number that is equal to the sum of its own digits each raised to the power of the number of digits.

---

**Input:**  
- An integer `n` (where `n ≥ 0`).

**Output:**  
- Return `True` if the number is an Armstrong number.  
- Return `False` otherwise.

---

**Example 1:**  
```text
Input:  
n = 153  

Output:  
True
```

**Example 2:**  
```text
Input:  
n = 9474  

Output:  
True
```

**Example 3:**  
```text
Input:  
n = 123  

Output:  
False
```

---

**Explanation:**  
- In **Example 1**, `153` has 3 digits. The sum of `1³ + 5³ + 3³ = 153`, so it is an Armstrong number.  
- In **Example 2**, `9474` has 4 digits. The sum of `9⁴ + 4⁴ + 7⁴ + 4⁴ = 9474`, so it is an Armstrong number.  
- In **Example 3**, `123` has 3 digits. The sum of `1³ + 2³ + 3³ = 36`, which is not equal to `123`, so it is not an Armstrong number.

"""



def num_of_digits(n):
    count = 0
    while n > 0:
        count+=1
        n //= 10
    return count


def is_armstrong(n):
    sums = 0
    count = num_of_digits(n)
    original_num = n
    while n > 0:
        digit = n % 10
        sums += digit**count
        n //= 10
    return original_num == sums
        
    




n = 153
print(is_armstrong(n))

