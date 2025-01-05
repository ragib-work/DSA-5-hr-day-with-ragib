"""
### **Problem Statement:**  
**Print the Matrix in a Zig-Zag Pattern**  
Given a matrix of size `m x n`, print its elements in a **zig-zag pattern**. The zig-zag pattern traverses the matrix row by row:  
- For the **first row**, traverse from left to right.  
- For the **second row**, traverse from right to left.  
- Continue alternating the direction for each subsequent row.

**Input:**  
- Two integers `m` and `n` representing the number of rows and columns, respectively.  
- A 2D list (matrix) with `m` rows and `n` columns.

**Output:**  
- A list of integers representing the elements of the matrix in a zig-zag pattern.

---

**Example:**  
```text
Input:  
m = 3, n = 4  
matrix = [[1, 2, 3, 4],  
          [5, 6, 7, 8],  
          [9, 1, 3, 2]]

Output:  
[1, 2, 3, 4, 8, 7, 6, 5, 9, 10, 11, 12]
```

---

**Explanation:**  
- **First row**: Left to right → `[1, 2, 3, 4]`  
- **Second row**: Right to left → `[8, 7, 6, 5]`  
- **Third row**: Left to right → `[9, 10, 11, 12]`  
- Combine the elements in order: `[1, 2, 3, 4, 8, 7, 6, 5, 9, 10, 11, 12]`

"""

def print_zigzag(matrix):
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        for j in range(n):
          if i%2 != 0:
            print(matrix[i][n-1-j], end=" ")
          else :
            print(matrix[i][j], end=" ")
        print()




matrix = [[1, 2, 3, 4],  
          [5, 6, 7, 8],  
          [9, 1, 3, 2]]
print_zigzag(matrix)


            