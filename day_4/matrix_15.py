"""
### **Problem Statement:**  
**Find the Inverse of a Matrix**  
Given a square matrix of size `n x n`, write a program to compute its **inverse**. A matrix `A` has an inverse `A⁻¹` if and only if the determinant of `A` is non-zero. If the matrix is invertible, compute the inverse matrix, otherwise return a message indicating that the matrix is not invertible.

**Input:**  
- An integer `n` representing the size of the matrix (number of rows and columns).  
- A 2D list (matrix) with `n` rows and `n` columns.

**Output:**  
- If the matrix is invertible, return the inverse of the matrix.  
- If the matrix is not invertible, return a message indicating that the matrix has no inverse.

---

### **Example 1:**
```text
Input:  
n = 2  
matrix = [[4, 7],  
          [2, 6]]

Output:  
Inverse Matrix:  
[[0.6, -0.7],  
 [-0.2, 0.4]]
```

---

### **Example 2:**
```text
Input:  
n = 2  
matrix = [[2, 4],  
          [1, 2]]

Output:  
Matrix is not invertible (determinant is 0).
```

---

### **Explanation:**
- **Example 1**: The determinant of the matrix is non-zero, so the matrix is invertible and the inverse is computed.
- **Example 2**: The determinant of the matrix is zero, indicating that the matrix does not have an inverse.

"""

def cal_determinant(matrix):
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        for j in range(n):
            if i == 0 :
                


def inverse_of_matrix(matrix):
    determinant = cal_determinant(matrix)
    transpose =  cal_transpose(matrix)


