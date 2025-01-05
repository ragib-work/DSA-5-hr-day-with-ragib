"""
### **Problem Statement:**  
**Print the Left and Right Diagonals of a Matrix**  
Given a square matrix of size `n x n`, print the elements of:  
1. **Left Diagonal**: The diagonal that starts from the top-left corner and ends at the bottom-right corner.  
2. **Right Diagonal**: The diagonal that starts from the top-right corner and ends at the bottom-left corner.

**Input:**  
- An integer `n` representing the size of the matrix (number of rows and columns).  
- A 2D list (matrix) with `n` rows and `n` columns.

**Output:**  
- A list of elements from the left diagonal.  
- A list of elements from the right diagonal.

**Example:**  
```text
Input:  
n = 3  
matrix = [[1, 2, 3],  
          [4, 5, 6],  
          [7, 8, 9]]

Output:  
Left Diagonal: [1, 5, 9]  
Right Diagonal: [3, 5, 7]
```

"""

def left_right_diagonal(matrix):
    # because it is a square matrix so both m and n is equal
    m = n = len(matrix)
    left = []
    right = []
    for i in range(m):
        for j in range(n):
            # for left diagonal
            if i == j :
                left.append(matrix[i][j])
            
            # for right diagonal
            if i+j == m-1:
                right.append(matrix[i][j])
    return left,right




matrix = [[1, 2, 3],  
          [4, 5, 6],  
          [7, 8, 9]]

print(left_right_diagonal(matrix))

