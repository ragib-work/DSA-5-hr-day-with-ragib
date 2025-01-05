"""
### **Problem Statement:**  
**Calculate the sum of each row and each column in a matrix.**  
Given a 2D matrix of size `m x n`, calculate the sum of the elements in each row and each column. Return the row sums and column sums as separate lists.

**Input:**  
- An integer `m` representing the number of rows.  
- An integer `n` representing the number of columns.  
- A 2D list (matrix) with `m` rows and `n` columns.

**Output:**  
- A list containing the sum of elements in each row.  
- A list containing the sum of elements in each column.

**Example:**  
```text
Input:  
m = 3, n = 3  
matrix = [[1, 2, 3],  
          [4, 5, 6],  
          [7, 8, 9]]

Output:  
Row sums: [6, 15, 24]  
Column sums: [12, 15, 18]
```

"""

def row_col_sum(matrix):
    m = len(matrix)
    n = len(matrix[0])
    row_sums = [0]* m
    col_sums = [0]* n
    for i in range(m):
        for j in range(n):
            row_sums[i] += matrix[i][j]
            col_sums[j] += matrix[i][j]
    return row_sums, col_sums



#---- running the above function -----------------
matrix = [[1, 2, 3],  
          [4, 5, 6],  
          [7, 8, 9]]
print(row_col_sum(matrix))



