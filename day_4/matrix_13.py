"""
### **Problem Statement:**  
**Check if a Matrix is an Identity Matrix**  
Given a square matrix of size `n x n`, check if it is an **identity matrix**. A matrix is considered an identity matrix if:  
- All the diagonal elements are `1`.  
- All the non-diagonal elements are `0`.

**Input:**  
- An integer `n` representing the size of the matrix (number of rows and columns).  
- A 2D list (matrix) with `n` rows and `n` columns.

**Output:**  
- Return `True` if the matrix is an identity matrix, otherwise return `False`.

---

**Example 1:**  
```text
Input:  
n = 3  
matrix = [[1, 0, 0],  
          [0, 1, 0],  
          [0, 0, 1]]

Output:  
True
```

---

**Example 2:**  
```text
Input:  
n = 3  
matrix = [[1, 0, 0],  
          [0, 1, 1],  
          [0, 0, 1]]

Output:  
False
```

---

**Explanation:**  
- In **Example 1**, all diagonal elements are `1` and all non-diagonal elements are `0`, so it is an identity matrix.  
- In **Example 2**, the non-diagonal element at position `[1][2]` is `1` instead of `0`, so it is not an identity matrix.

"""


def is_identity_matrix(matrix):
    m = len(matrix)
    n = len(matrix[0])

    for i in range(m):
        for j in range(n):
            # checking for diagonal element ( i == j )
            if i == j and matrix[i][j] != 1 :
                return False
            # other than diagonal element (i != j )
            elif i != j and matrix[i][j] != 0 :
                return False
    return True



matrix = [[1, 0, 0],  
          [0, 1, 0],  
          [0, 0, 1]]

print(is_identity_matrix(matrix))
