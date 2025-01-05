"""
### **Problem Statement:**  
**Find the maximum and minimum values in each row of a matrix.**  
Given a 2D matrix of size `m x n`, for each row of the matrix, find the maximum and minimum values. Return two lists: one containing the maximum values of each row, and the other containing the minimum values of each row.

**Input:**  
- An integer `m` representing the number of rows.  
- An integer `n` representing the number of columns.  
- A 2D list (matrix) with `m` rows and `n` columns.

**Output:**  
- A list containing the maximum values of each row.
- A list containing the minimum values of each row.

**Example:**  
```text
Input:  
m = 3, n = 3  
matrix = [[1, 2, 3],  
          [4, 5, 6],  
          [7, 8, 9]]

Output:  
Max values: [3, 6, 9]  
Min values: [1, 4, 7]
```

"""

def max_min_in_row(matrix):
    max_values = []
    min_values = []
    for row in matrix:
        max_val = float('-inf')
        min_val = float('inf')
        for col in row:
            if col > max_val:
                max_val = col
            if col < min_val:
                min_val = col
        max_values.append(max_val)
        min_values.append(min_val)
    return max_values , min_values



matrix = [[1, 2, 3],  
          [4, 5, 6],  
          [7, 8, 9]]
print(max_min_in_row(matrix))
            