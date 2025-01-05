"""
### **Problem Statement:**  
**Find the maximum and minimum values in each column of a matrix.**  
Given a 2D matrix of size `m x n`, for each column of the matrix, find the maximum and minimum values. Return two lists: one containing the maximum values of each column, and the other containing the minimum values of each column.

**Input:**  
- An integer `m` representing the number of rows.  
- An integer `n` representing the number of columns.  
- A 2D list (matrix) with `m` rows and `n` columns.

**Output:**  
- A list containing the maximum values of each column.
- A list containing the minimum values of each column.

**Example:**  
```text
Input:  
m = 3, n = 3  
matrix = [[1, 2, 3],  
          [4, 5, 6],  
          [7, 8, 9]]

Output:  
Max values: [7, 8, 9]  
Min values: [1, 2, 3]
```
"""

def max_min_in_cols(matrix):
    m = len(matrix)
    n = len(matrix[0])
    max_val = float('-inf')
    min_val = float('inf')
    max_values = [max_val]*n
    min_values = [min_val]*n
    for i in range(m): 
        for j in range(n):
            if matrix[i][j] > max_values[j]:
                max_values[j] = matrix[i][j]
            if matrix[i][j] < min_values[j]:
                min_values[j] = matrix[i][j]
    
    return max_values , min_values



matrix = [[1, 2, 3],  
          [4, 5, 6],  
          [7, 8, 9]]
print(max_min_in_cols(matrix))