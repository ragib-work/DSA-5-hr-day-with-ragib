"""
### **Problem Statement:**  
**Check if a Matrix is Sparse**  
Given a matrix of size `m x n`, determine whether it is a **sparse matrix**. A matrix is considered sparse if **more than half of its elements are zero**.

**Input:**  
- Two integers `m` and `n` representing the number of rows and columns, respectively.  
- A 2D list (matrix) with `m` rows and `n` columns.

**Output:**  
- Return `True` if the matrix is sparse, otherwise return `False`.

---

**Example 1:**  
```text
Input:  
m = 3, n = 3  
matrix = [[0, 0, 0],  
          [1, 0, 0],  
          [0, 0, 2]]

Output:  
True
```

---

**Example 2:**  
```text
Input:  
m = 2, n = 2  
matrix = [[1, 0],  
          [3, 4]]

Output:  
False
```

---

**Explanation:**  
- In **Example 1**, the matrix has 9 elements, of which 7 are zeroes (more than half). Therefore, it is a sparse matrix.  
- In **Example 2**, the matrix has 4 elements, of which only 1 is zero (less than half). Therefore, it is not a sparse matrix.

"""

def is_sparse_matrix(matrix):
    m = len(matrix)
    n = len(matrix[0])
    count_zeros = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                count_zeros+=1
    
    if count_zeros > m*n/2:
        return True
    else:
        return False
    


matrix = [[1, 0],  
          [3, 4]]
print(is_sparse_matrix(matrix))