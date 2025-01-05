"""
### **Problem Statement:**  
**Print the Boundary Elements of a Matrix**  
Given a matrix of size `m x n`, print the elements that lie on its **boundary**. The boundary elements include:  
- The elements in the **first row**.  
- The elements in the **last row**.  
- The elements in the **first column** (excluding the corners if already printed).  
- The elements in the **last column** (excluding the corners if already printed).

**Input:**  
- Two integers `m` and `n` representing the number of rows and columns, respectively.  
- A 2D list (matrix) with `m` rows and `n` columns.

**Output:**  
- A list of integers representing the boundary elements in the order they appear.

---

**Example:**  
```text
Input:  
m = 4, n = 4  
matrix = [[1, 2, 3, 4],  
          [5, 6, 7, 8],  
          [9, 10, 11, 12],  
          [13, 14, 15, 16]]

Output:  
[1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5]
```

---

**Example (for a non-square matrix):**  
```text
Input:  
m = 3, n = 5  
matrix = [[1, 2, 3, 4, 5],  
          [6, 7, 8, 9, 10],  
          [11, 12, 13, 14, 15]]

Output:  
[1, 2, 3, 4, 5, 10, 15, 14, 13, 12, 11, 6]
```

"""

def boundary_elem(matrix):
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        for j in range(n):
            if j == 0 or j == n-1:
                print(matrix[i][j], end=" ")
            elif i == 0  or i == m-1:
                print(matrix[i][j], end=" ")
            else:
                print("*", end=" ")
        print()




matrix = [[1, 2, 3, 4, 5],  
          [6, 7, 8, 9, 1],  
          [0, 1, 3, 2, 9],
          [9, 2, 7, 3, 5],
          [5, 4, 6, 1, 2]]
boundary_elem(matrix)