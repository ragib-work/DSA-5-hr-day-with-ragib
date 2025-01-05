"""
### **Problem Statement:**  
**Check if a Matrix is Symmetric**  
Given a square matrix of size `n x n`, check if it is **symmetric**. A matrix is symmetric if it is equal to its **transpose**. In other words, for a matrix `A`, it is symmetric if `A[i][j] == A[j][i]` for all valid `i` and `j`.

**Input:**  
- An integer `n` representing the size of the matrix (number of rows and columns).  
- A 2D list (matrix) with `n` rows and `n` columns.

**Output:**  
- Return `True` if the matrix is symmetric, otherwise return `False`.

---

**Example 1:**  
```text
Input:  
n = 3  
matrix = [[1, 2, 3],  
          [2, 5, 6],  
          [3, 6, 9]]

Output:  
True
```

---

**Example 2:**  
```text
Input:  
n = 3  
matrix = [[1, 0, 3],  
          [2, 5, 6],  
          [3, 6, 9]]

Output:  
False
```

---

**Explanation:**  
- In **Example 1**, the matrix is equal to its transpose, so it is symmetric.  
- In **Example 2**, the matrix is not equal to its transpose, so it is not symmetric.

"""

def is_matrix_symmetric(matrix):
    m = len(matrix)
    n = len(matrix[0])
    
    for i in range(m):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                return False
            
    return True
            




matrix = [[1, 2, 3],  
          [2, 5, 6],  
          [3, 6, 9]]

print(is_matrix_symmetric(matrix))
