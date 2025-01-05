"""
### **Problem Statement:**  
**Add and subtract two matrices.**  
Given two matrices `A` and `B` of size `m x n`, perform the following operations:
1. **Matrix Addition:** Add matrices `A` and `B` element-wise. Return the resulting matrix.
2. **Matrix Subtraction:** Subtract matrix `B` from matrix `A` element-wise. Return the resulting matrix.

**Input:**  
- An integer `m` representing the number of rows.  
- An integer `n` representing the number of columns.  
- Two 2D lists (matrices) `A` and `B`, both with dimensions `m x n`.

**Output:**  
- A 2D list (matrix) representing the result of matrix addition.
- A 2D list (matrix) representing the result of matrix subtraction.

**Example:**  
```text
Input:  
m = 3, n = 3  
Matrix A = [[1, 2, 3],  
            [4, 5, 6],  
            [7, 8, 9]]

Matrix B = [[9, 8, 7],  
            [6, 5, 4],  
            [3, 2, 1]]

Output:  
Matrix Addition:  
[[10, 10, 10],  
 [10, 10, 10],  
 [10, 10, 10]]  

Matrix Subtraction:  
[[-8, -6, -4],  
 [-2, 0, 2],  
 [4, 6, 8]]
```

"""


def add_sub_matrix(A,B):
    m = len(A)
    n = len(A[0])
    add = []
    sub = []
    for i in range(m):
        add.append([0]*n)
        sub.append([0]*n)
        for j in range(n):
            add[i][j] = A[i][j]+B[i][j]
            sub[i][j] = A[i][j]-B[i][j]
    
    return add , sub



A = [[1, 2, 3],  
    [4, 5, 6],  
    [7, 8, 9]]

B = [[9, 8, 7],  
    [6, 5, 4],  
    [3, 2, 1]]
        
print(add_sub_matrix(A,B))